#!/bin/sh

# fill this in or provide from environ
[ ! "$CODESIGN_IDENTITY" ] && CODESIGN_IDENTITY="UNKNOWN"

# program specifics
APP_NAME="Taxi2.2"
APP_IDENTIFIER="org.itaxotools.taxi2.gui"
APP_SCRIPT="run.py"
APP_ENTITLEMENTS="data/entitlements.plist"
APP_ICON_ICNS="data/taxi2.icns"
APP_ICON_ICO="data/taxi2.ico"

# expand and export
export CODESIGN_IDENTITY=$CODESIGN_IDENTITY
export APP_NAME="$APP_NAME"
export APP_IDENTIFIER="$APP_IDENTIFIER"

export APP_FILENAME="$APP_NAME"
export APP_SUFFIX=$(IFS=-; echo "$*")
if [ -n "$APP_SUFFIX" ]; then
    export APP_FILENAME="$APP_NAME-$APP_SUFFIX"
fi

DIR="$(cd "$(dirname "$0")" && pwd)"
export APP_SCRIPT="$DIR/$APP_SCRIPT"
export APP_ENTITLEMENTS="$DIR/$APP_ENTITLEMENTS"
export APP_ICON_ICNS="$DIR/$APP_ICON_ICNS"
export APP_ICON_ICO="$DIR/$APP_ICON_ICO"

export APP_BUNDLE="$PWD/dist/$APP_NAME.app"
export APP_IMAGE="$PWD/dist/$APP_FILENAME.dmg"
