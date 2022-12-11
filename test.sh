#!/bin/zsh
#pyinstaller --onefile --nowindow -p . sub-ts.py
cd dist
rm sub-ts-macos.zip && zip sub-ts-macos.zip sub-ts config.yaml
cd ..
rm docker/src/*.py
cp sub-ts.py SubTranslator.py docker/src/
cd docker/src && docker run -v "$(pwd):/src/" --entrypoint /bin/sh cdrx/pyinstaller-windows:latest -c "python -m pip install --upgrade pip && /entrypoint.sh"
cd dist/windows && rm sub-ts-win.zip
zip sub-ts-windows.zip sub-ts.exe config.yaml
