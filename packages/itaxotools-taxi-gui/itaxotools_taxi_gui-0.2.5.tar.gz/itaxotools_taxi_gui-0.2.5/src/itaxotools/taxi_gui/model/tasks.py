# -----------------------------------------------------------------------------
# TaxiGui - GUI for Taxi2
# Copyright (C) 2022-2023  Patmanidis Stefanos
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# -----------------------------------------------------------------------------

from PySide6 import QtCore

import itertools
from collections import defaultdict
from pathlib import Path
from tempfile import TemporaryDirectory
from typing import Callable, List

from itaxotools.common.bindings import Binder, Instance, Property, PropertyRef
from itaxotools.taxi_gui import app

from ..threading import (
    DataQuery,
    ReportDone,
    ReportExit,
    ReportFail,
    ReportProgress,
    ReportStop,
    Worker,
)
from ..types import ChildAction, Notification
from .common import Object


class ActionMenu(Object):
    actions = Property(list[ChildAction], [])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.actions: list[ChildAction] = []

    def add(self, key: str, label: str, tip: str):
        action = ChildAction(key, label, tip)
        self.actions.append(action)
        self.properties.actions.update()

    def clear(self):
        self.actions.clear()
        self.properties.actions.update()


class TaskModel(Object):
    task_name = "Task"

    notification = QtCore.Signal(Notification)
    progression = QtCore.Signal(ReportProgress)
    query = QtCore.Signal(DataQuery)

    show_open = Property(bool, False)
    show_save = Property(bool, False)
    show_export = Property(bool, False)

    can_open = Property(bool, False)
    can_save = Property(bool, True)
    can_export = Property(bool, False)
    can_start = Property(bool, True)
    can_stop = Property(bool, False)

    menu_open = Property(ActionMenu, Instance)
    menu_save = Property(ActionMenu, Instance)
    menu_export = Property(ActionMenu, Instance)

    ready = Property(bool, True)
    busy = Property(bool, False)
    busy_subtask = Property(bool, False)
    done = Property(bool, False)
    editable = Property(bool, True)

    suggested_directory = Property(Path, Path())

    counters = defaultdict(lambda: itertools.count(1, 1))

    def __init__(self, name=None, daemon=True):
        super().__init__(name or self._get_next_name())
        self.binder = Binder()

        self.show_open = app.config.show_open
        self.show_save = app.config.show_save
        self.show_export = app.config.show_export

        self.temporary_directory = TemporaryDirectory(prefix=f"{self.task_name}_")
        self.temporary_path = Path(self.temporary_directory.name)

        self.worker = Worker(
            name=self.name,
            eager=True,
            daemon=daemon,
            log_path=self.temporary_path,
        )

        self.binder.bind(
            self.worker.done, self.onDone, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.fail, self.onFail, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.error, self.onError, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.stop, self.onStop, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.query, self.query.emit, condition=self._matches_report_id
        )
        self.binder.bind(self.worker.progress, self.progression.emit)

        for property in [
            self.properties.done,
            self.properties.busy,
            self.properties.busy_subtask,
        ]:
            property.notify.connect(self.checkEditable)
            property.notify.connect(self.checkRunnable)
            property.notify.connect(self.checkStopable)

    def __repr__(self):
        return f"{self.task_name}({repr(self.name)})"

    @classmethod
    def _get_next_name(cls):
        # return f'{cls.task_name} #{next(cls.counters[cls.task_name])}'
        return cls.task_name

    def _matches_report_id(self, report) -> bool:
        if not hasattr(report, "id"):
            return False
        return report.id == id(self)

    def onFail(self, report: ReportFail):
        self.notification.emit(
            Notification.Fail(str(report.exception), report.traceback)
        )
        self.busy = False

    def onError(self, report: ReportExit):
        self.notification.emit(
            Notification.Fail(f"Process failed with exit code: {report.exit_code}")
        )
        self.busy = False

    def onStop(self, report: ReportStop):
        self.notification.emit(Notification.Warn("Cancelled by user."))
        self.busy = False

    def onDone(self, report: ReportDone):
        """Overload this to handle results"""
        self.notification.emit(
            Notification.Info(f"{self.name} completed successfully!")
        )
        self.busy = False
        self.done = True

    def start(self):
        """Slot for starting the task"""
        self.progression.emit(ReportProgress("Preparing for execution..."))
        self.busy = True

    def stop(self):
        """Slot for interrupting the task"""
        if self.worker is None:
            return
        self.worker.reset()

    def open(self, path: Path, key=None):
        """Slot for opening files"""

    def save(self, path: Path, key=None):
        """Slot for saving results"""

    def export(self, path: Path, key=None):
        """Slot for exporting results"""

    def clear(self):
        """Slot for discarding results"""
        self.done = False

    def readyTriggers(self) -> List[PropertyRef]:
        """Overload this to set properties as ready triggers"""
        return []

    def checkReady(self):
        """Slot to check if ready"""
        self.ready = self.isReady()

    def isReady(self) -> bool:
        """Overload this to check if ready"""
        return False

    def answer(self, data):
        """Slot for answering queries"""
        self.worker.answer(data)

    def checkEditable(self):
        self.editable = not (self.busy or self.busy_subtask or self.done)

    def checkRunnable(self):
        self.can_start = not (self.busy or self.busy_subtask or self.done)

    def checkStopable(self):
        self.can_stop = self.busy or self.busy_subtask

    def exec(self, task: Callable, *args, **kwargs):
        """Call this from start() to execute tasks"""
        self.worker.exec(id(self), task, *args, **kwargs)


class SubtaskModel(Object):
    task_name = "Subtask"

    notification = QtCore.Signal(Notification)
    progression = QtCore.Signal(ReportProgress)
    query = QtCore.Signal(DataQuery)

    busy = Property(bool, False)

    counters = defaultdict(lambda: itertools.count(1, 1))

    def __init__(self, parent: TaskModel, name=None, bind_busy=True):
        super().__init__(name or self._get_next_name())
        self.binder = Binder()

        self.temporary_path = parent.temporary_path
        self.worker = parent.worker
        self._autostart_task = None
        self._autostart_args = None
        self._autostart_kwargs = None

        self.binder.bind(
            self.worker.done, self.onDone, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.fail, self.onFail, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.error, self.onError, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.stop, self.onStop, condition=self._matches_report_id
        )
        self.binder.bind(
            self.worker.query, self.query.emit, condition=self._matches_report_id
        )
        self.binder.bind(self.worker.progress, self.progression.emit)

        self.binder.bind(self.worker.process_started, self._on_process_started)

        self.binder.bind(self.notification, parent.notification)
        self.binder.bind(self.progression, parent.progression)
        self.binder.bind(self.query, parent.query)

        if bind_busy:
            self.binder.bind(self.properties.busy, parent.properties.busy_subtask)

    def __repr__(self):
        return f"{self.task_name}({repr(self.name)})"

    @classmethod
    def _get_next_name(cls):
        return f"{cls.task_name} #{next(cls.counters[cls.task_name])}"

    def _matches_report_id(self, report) -> bool:
        if not hasattr(report, "id"):
            return False
        return report.id == id(self)

    def _on_process_started(self):
        if self._autostart_task:
            self.start(
                self._autostart_task, *self._autostart_args, **self._autostart_kwargs
            )

    def onFail(self, report: ReportFail):
        self.notification.emit(
            Notification.Fail(str(report.exception), report.traceback)
        )
        self.busy = False

    def onError(self, report: ReportExit):
        self.notification.emit(
            Notification.Fail(f"Process failed with exit code: {report.exit_code}")
        )
        self.busy = False

    def onStop(self, report: ReportStop):
        self.notification.emit(Notification.Warn("Cancelled by user."))
        self.busy = False

    def onDone(self, report: ReportDone):
        """Overload this to handle results"""
        # self.notification.emit(Notification.Info(f'{self.name} completed successfully!'))
        self.busy = False

    def start(self, task: Callable, *args, **kwargs):
        """Slot for starting the task"""
        self.progression.emit(ReportProgress("Preparing for execution..."))
        self.busy = True
        self.exec(task, *args, **kwargs)

    def autostart(self, task: Callable, *args, **kwargs):
        """Slot for setting a task to autostart with the worker"""
        self._autostart_task = task
        self._autostart_args = args
        self._autostart_kwargs = kwargs

    def stop(self):
        """Slot for interrupting the task"""
        if self.worker is None:
            return
        self.worker.reset()

    def exec(self, task: Callable, *args, **kwargs):
        """Call this from start() to execute tasks"""
        self.worker.exec(id(self), task, *args, **kwargs)

    def answer(self, data):
        """Slot for answering queries"""
        self.worker.answer()
