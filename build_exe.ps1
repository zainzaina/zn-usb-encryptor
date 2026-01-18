# Build the GUI into a single .exe using PyInstaller
Param(
    [string]$VenvActivate = '.\.venv\Scripts\Activate.ps1'
)

if (Test-Path $VenvActivate) {
    Write-Output "Activating virtualenv: $VenvActivate"
    & $VenvActivate
}

Write-Output 'Installing pyinstaller (if needed) and building...'
pip install pyinstaller

# Build one-file, windowed (no console) executable
pyinstaller --onefile --noconsole --name SecureEncryptor secure_encryptor_gui.py

if (Test-Path '.\dist\SecureEncryptor.exe') {
    Write-Output 'Build succeeded. Dist: .\dist\SecureEncryptor.exe'
} else {
    Write-Output 'Build finished but .exe not found. Check PyInstaller output.'
}
