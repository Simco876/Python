import subprocess
import keyboard
import time
import ctypes
import os
import sys

# Path to the PDF file
pdf_file = r'C:\Labels\TYA_.pdf'

# Full path to SumatraPDF.exe
sumatra_path = r'C:\Program Files\SumatraPDF\SumatraPDF.exe'

# Command to print the PDF using SumatraPDF and switch to landscape
command = f'"{sumatra_path}" -print-to-default -print-settings "landscape" "{pdf_file}"'

# Path to the lock file
lock_file = r'C:\Labels\lockfile.lck'

# Function to run the print command
def print_pdf():
    try:
        print(f"Running command: {command}")
        # Run the print command
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        print(f"Command output: {result.stdout}")
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        else:
            print("Print command executed successfully.")
    except Exception as e:
        print(f"Exception occurred: {e}")

# Function to minimize the console window
def minimize_console():
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

# Function to check for the lock file and restart the script if it exists
def check_lock_file():
    if os.path.exists(lock_file):
        print("Lock file found. Restarting script...")
        # Restart the script
        python = sys.executable
        os.execv(python, ['python'] + sys.argv)

# Function to handle the hotkey action
def hotkey_action():
    # Disable the hotkey to prevent re-triggering
    keyboard.remove_hotkey('alt+p')
    check_lock_file()
    print_pdf()
    # Re-enable the hotkey after the print command is executed
    keyboard.add_hotkey('alt+p', hotkey_action)

# Initial hotkey setup
keyboard.add_hotkey('alt+p', hotkey_action)

# Minimize the console window
minimize_console()

# Keep the script running indefinitely
print("Press Alt+P to print the PDF.")
while True:
    check_lock_file()
    time.sleep(1)  # Keep the script running

# Keep the window open
input("Press Enter to exit...")
