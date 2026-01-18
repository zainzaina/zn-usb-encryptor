@echo off
REM Build the GUI into a single .exe using PyInstaller (Windows cmd)
if exist ".venv\Scripts\activate.bat" (
    call .venv\Scripts\activate.bat
)

@echo Installing pyinstaller (if needed) and building...
pip install pyinstaller
pyinstaller --onefile --noconsole --name SecureEncryptor secure_encryptor_gui.py

if exist dist\SecureEncryptor.exe (
    echo Build succeeded. Dist: dist\SecureEncryptor.exe
) else (
    echo Build finished but dist\SecureEncryptor.exe not found. Check PyInstaller output.
)
