Secure USB Encryption Tool

A lightweight, GUI-based file encryption tool that secures files using two-factor protection:
a user-defined password and a cryptographic key stored on a USB flash drive.

This project is designed for personal and educational use, demonstrating practical file encryption, key derivation, and physical key-based access control.

Overview

Secure USB Encryption Tool encrypts and decrypts files by deriving a strong encryption key from:

A user password

A binary key file (usb.key) stored on a removable USB drive

Access to encrypted files is impossible unless both factors are present.

The application provides a simple graphical interface built with tkinter and uses the cryptography library for secure encryption primitives.

Key Features

Two-factor access control (Password + USB key file)

GUI-based encryption and decryption

Encrypts a single file and replaces it with the encrypted version

Decrypts files only when the correct password and USB key are present

Automatically locks when the USB drive is removed

Manual lock/unlock controls

Basic activity logging (activity.log)

Optional standalone Windows executable build

Security Model (High-Level)

Encryption keys are never stored on disk

Final encryption key is derived from:

User password

Contents of usb.key

Removing the USB drive immediately revokes access

Loss of the USB key or password results in permanent data loss

This tool is intended for learning and personal use.
It is not a replacement for enterprise-grade disk encryption solutions.

Requirements

Python 3.8 or later

cryptography

tkinter (included with most Python installations)

Install dependencies:

pip install cryptography


Or:

pip install -r requirements.txt

Installation & Usage (Windows)
1. (Optional) Create a virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

2. Run the application
python secure_encryptor_gui.py

USB Key Setup

The application requires a binary key file named usb.key stored on a USB flash drive.

Create the USB key (Python)
python - <<'PY'
import os
open('E:/usb.key','wb').write(os.urandom(32))
print('usb.key created on E:')
PY

Create the USB key (PowerShell)
$bytes = New-Object byte[] 32
(New-Object System.Security.Cryptography.RNGCryptoServiceProvider).GetBytes($bytes)
[IO.File]::WriteAllBytes('E:\usb.key',$bytes)

Configure the path

In secure_encryptor_gui.py, update the USB key path if needed:

USB_KEY_PATH = "E:/usb.key"

GUI Workflow

Insert the USB flash drive containing usb.key

Enter your password

Click Unlock

Use Encrypt File or Decrypt File

Click Lock to manually lock the application
(automatic lock occurs if the USB drive is removed)

Activity Logging

All major actions are logged to:

activity.log


Located in the project directory.

Backup & Safety Notes

Always back up your usb.key

If the USB key or password is lost, encrypted files cannot be recovered

Files are overwritten during encryption—create backups before testing

Helper Scripts

Included utility files:

requirements.txt

create_usb_key.py

create_usb_key.ps1

build_exe.ps1

build_exe.bat

Create a USB key via script:

python create_usb_key.py --drive E:


Or:

.\create_usb_key.ps1 -Drive 'E:'

Building a Standalone EXE (Windows)

Requirements:

Python

Dependencies from requirements.txt (includes pyinstaller)

PowerShell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
.\build_exe.ps1

Command Prompt
\.venv\Scripts\activate.bat
pip install -r requirements.txt
build_exe.bat


Output:

dist\SecureEncryptor.exe

Contribution

Contributions are welcome, including:

UI/UX improvements

Folder encryption support

Non-destructive encryption modes

Security hardening

Please credit the original author and do not redistribute without acknowledgment.

License

Free for personal and educational use only.
If you modify or reuse this project, attribution is required.
