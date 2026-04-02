#!/bin/bash
# Исправление pyjnius config.pxi
PYJNIUS_DIR=$(find .buildozer/android/platform/build-*/build/other_builds/pyjnius-sdl2 -type d -name "pyjnius" | head -n1)
if [ -n "$PYJNIUS_DIR" ]; then
    echo "Исправляем pyjnius в $PYJNIUS_DIR"
    # Добавляем DEF JNIUS_PLATFORM = "android" в начало config.pxi
    sed -i '1i DEF JNIUS_PLATFORM = "android"' "$PYJNIUS_DIR/jnius/config.pxi"
else
    echo "Папка pyjnius не найдена"
fi