import os
import sys
import time
import threading
import logging
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.fernet import Fernet
import base64

# ================= CONFIG =================
USB_KEY_PATH = "E:/usb.key"   # غيّري حرف الفلاشة عندك
LOG_FILE = "activity.log"
CHECK_INTERVAL = 2  # seconds
# =========================================

# ================ LOGGING =================
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
# =========================================

locked = True
fernet = None
monitor_thread = None

# ============ CRYPTO HELPERS ==============
def derive_key(password: str, usb_key_bytes: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=usb_key_bytes,
        iterations=100000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def load_usb_key():
    if not os.path.exists(USB_KEY_PATH):
        return None
    with open(USB_KEY_PATH, "rb") as f:
        return f.read()
# =========================================

# =============== CORE LOGIC ===============
def lock_app():
    global locked, fernet
    locked = True
    fernet = None
    status_label.config(text="Status: LOCKED", fg="red")
    logging.warning("Application locked (USB removed or manual lock).")

def unlock_app():
    global locked, fernet

    password = password_entry.get()
    if not password:
        messagebox.showerror("Error", "Password required.")
        return

    usb_key = load_usb_key()
    if usb_key is None:
        messagebox.showerror("Error", "USB key not detected.")
        return

    try:
        key = derive_key(password, usb_key)
        fernet = Fernet(key)
        locked = False
        status_label.config(text="Status: UNLOCKED", fg="green")
        logging.info("Application unlocked successfully.")
    except Exception:
        messagebox.showerror("Error", "Failed to unlock.")
        logging.error("Unlock failed.")

def encrypt_file():
    if locked:
        messagebox.showerror("Locked", "Unlock the app first.")
        return

    path = filedialog.askopenfilename()
    if not path:
        return

    with open(path, "rb") as f:
        data = f.read()

    encrypted = fernet.encrypt(data)

    with open(path, "wb") as f:
        f.write(encrypted)

    logging.info(f"File encrypted: {path}")
    messagebox.showinfo("Success", "File encrypted.")

def decrypt_file():
    if locked:
        messagebox.showerror("Locked", "Unlock the app first.")
        return

    path = filedialog.askopenfilename()
    if not path:
        return

    with open(path, "rb") as f:
        data = f.read()

    try:
        decrypted = fernet.decrypt(data)
    except Exception:
        messagebox.showerror("Error", "Invalid key or corrupted file.")
        logging.error("Decryption failed.")
        return

    with open(path, "wb") as f:
        f.write(decrypted)

    logging.info(f"File decrypted: {path}")
    messagebox.showinfo("Success", "File decrypted.")
# =========================================

# ============ USB MONITOR THREAD ==========
def monitor_usb():
    global locked
    while True:
        if not os.path.exists(USB_KEY_PATH) and not locked:
            lock_app()
            messagebox.showwarning("USB Removed", "USB key removed. App locked.")
        time.sleep(CHECK_INTERVAL)
# =========================================

# ================= GUI ====================
app = tk.Tk()
app.title("Secure USB Encryption Tool")
app.geometry("420x320")
app.resizable(False, False)

tk.Label(app, text="Password:", font=("Arial", 11)).pack(pady=5)
password_entry = tk.Entry(app, show="*", width=30)
password_entry.pack()

tk.Button(app, text="Unlock", width=25, command=unlock_app).pack(pady=5)
tk.Button(app, text="Lock", width=25, command=lock_app).pack(pady=5)

tk.Button(app, text="Encrypt File", width=25, command=encrypt_file).pack(pady=5)
tk.Button(app, text="Decrypt File", width=25, command=decrypt_file).pack(pady=5)

status_label = tk.Label(app, text="Status: LOCKED", fg="red", font=("Arial", 12))
status_label.pack(pady=10)

# Start USB monitoring thread
monitor_thread = threading.Thread(target=monitor_usb, daemon=True)
monitor_thread.start()

app.mainloop()
# =========================================
