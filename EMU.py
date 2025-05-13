import os

# ------------------- SYSTEM FOLDERS ------------------

# Set where to look for the builds to test
# Options: usb (for USB-drive having 'EMU' label), current (for current application folder)
source_folder = "current"

# Set traces folder (the folder that esoTraceViewer collects traces to)
traces_folder = os.path.join(os.environ['USERPROFILE'], 'Documents', 'logs')

# Set screenshots folder
screenshots_folder = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'Screenshots')

# Set path to 7-zip
zip_path = r"C:\Program Files\7-Zip\7z.exe"

# Set path to Android SDK
android_sdk_folder = os.path.join(os.environ['USERPROFILE'], 'AppData', 'Local', 'Android', 'Sdk')

# Set path to system images folder
system_images_folder = os.path.join(android_sdk_folder, 'system-images')

# Set path to emulator folder
emulator_folder = os.path.join(android_sdk_folder, 'emulator')

# Set path to virtual device folder
virtual_device_folder = os.path.join(os.environ['USERPROFILE'], '.android', 'avd')

# Print the paths to verify
print(f"Source Folder: {source_folder}")
print(f"Traces Folder: {traces_folder}")
print(f"Screenshots Folder: {screenshots_folder}")
print(f"7-Zip Path: {zip_path}")
print(f"Android SDK Folder: {android_sdk_folder}")
print(f"System Images Folder: {system_images_folder}")
print(f"Emulator Folder: {emulator_folder}")
print(f"Virtual Device Folder: {virtual_device_folder}")

# ------------------- OTHER SETTINGS ------------------

# Set emulator window width and height in pixels
emulator_window_width = 800
emulator_window_height = 415

# Set for how long to wait till device boots up (in minutes)
boot_timeout_minutes = 5

# Set whether to always skip 'app grid visible' test case
app_grid_visible_always_skip = False

# Set for how long to wait till app grid or app opens in 'app grid visible' test case (in minutes)
app_grid_wait_minutes = 3

# Enable or disable sound notifications for required user actions
sound = "enabled"

# Set device name
device_name = "OIA"

# Set device profile name
device_profile_name = "OIA"

# -----------------------------------------------------
# ------------------ END OF SETTINGS ------------------
# -----------------------------------------------------

# Set app version
version = "1.3"

# Device characteristics
diagonal_length = 10.10
screen_size = "xlarge"
pixel_density = "mdpi"
xdpi = 160
ydpi = 160
screen_width = 1540
screen_height = 800
tag = "android-automotive"
ram = 4096

# Process source_folder
source_folder = "current"  # Assuming 'current' as default
source_folder_display = "in current folder" if source_folder == "current" else "on EMU USB-drive"

# Adjust window size
# Note: Python does not have a direct equivalent to 'mode con: cols=120', but you can use libraries like curses for terminal manipulation

# Set window title
window_title = f"EMU Tester {version}"

# Show logo
# Note: Implement a function to display the logo if needed

# Set title message
title = "Emu - flightless bird of Australia - is the second largest living bird"

# Light colors with foreground and background
colors = {
    "blue1": "[94m",
    "blue2": "[104m",
    "cyan1": "[96m",
    "cyan2": "[106m",
    "gray1": "[37m",
    "gray2": "[107m",
    "green1": "[92m",
    "green2": "[102m",
    "magenta1": "[95m",
    "magenta2": "[105m",
    "red1": "[91m",
    "red2": "[101m",
    "yellow1": "[93m",
    "yellow2": "[103m",
    "white": "[97m",
    "black_font": "[30m",
    "black_back": "[40m",
    "darkblue1": "[34m",
    "darkblue2": "[44m",
    "darkcyan1": "[36m",
    "darkcyan2": "[46m",
    "darkgray1": "[90m",
    "darkgray2": "[100m",
    "darkgreen1": "[32m",
    "darkgreen2": "[42m",
    "darkmagenta1": "[35m",
    "darkmagenta2": "[45m",
    "darkred1": "[31m",
    "darkred2": "[41m",
    "darkyellow1": "[33m",
    "darkyellow2": "[43m",
    "bold": "[1m",
    "nocolor": "[0m"
}

# Define title color options
color_1 = title[9]
color_2 = title[42]
color_3 = title[40]
color_4 = title[4]
color_5 = title[20]
color_6 = title[30]
color_7 = title[11]
color_8 = title[13]

color = f"{color_1}{color_2}{color_3}{color_4}{color_5}{color_6}{color_7}{color_8}"

# Define correct spelling
boot_minute_s = "minute" if boot_timeout_minutes == 1 else "minutes"

# Define escape symbol to use colors in text
ESC = "\033"

offset = 0
pattern = "^ .\.\ d4$"
offset += 1

# Set delay between printing each character with 'say' function
delay = 10

format = "HH:mm dd.MM.yyyy"

# Define colors of operations
# Note: Implement a function to define colors if needed

# Check free space on system disk
# Note: Implement a function to check free space if needed

# Check if Java is available and get its Java version
# Note: Implement a function to check Java if needed

# Check if Command-line Tools are available and get their folder
# Note: Implement a function to check Command-line Tools if needed

# ADB devices check
# Note: Implement a function to check ADB devices if needed

# Flag showing if device failed to boot, set by 'wait_for_boot' function
device_failed_to_boot = False

# Get assignee name in Jira
# Note: Implement a function to get assignee if needed