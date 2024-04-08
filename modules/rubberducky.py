print(f"[*]     Importing RubberDucky Modules...")
import time
start_time = time.monotonic()

import os
import sys
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ducky

end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
num_modules = len(sys.modules)
print(f"[*]     Imported {num_modules} Modules [{execution_time}ms]")

def rubberducky(payload_path):
    start_time = time.monotonic()
    time.sleep(1)
    keyboard = Keyboard(usb_hid.devices)
    keyboard_layout = KeyboardLayoutUS(keyboard)
    end_time = time.monotonic()
    execution_time = (end_time - start_time) * 1000
    print(f"[*] Setup KEYBOARD [{execution_time}ms]")

    start_time = time.monotonic()
    duck = adafruit_ducky.Ducky(payload_path, keyboard, keyboard_layout)
    with open(payload_path, 'rb') as payload:
        payload.seek(0, 2)
        payload_size = payload.tell()
    end_time = time.monotonic()
    execution_time = (end_time - start_time) * 1000
    print(f"[*] Loaded Payload. [{payload_path}] [{payload_size}B] [{execution_time}ms]")

    start_time = time.monotonic()
    print("[*] Executing Payload...")
    result = True
    while result is not False:
        result = duck.loop()