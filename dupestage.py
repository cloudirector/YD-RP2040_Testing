print(f"[*] Importing Modules...")
import time
start_time = time.monotonic()
import sys
import usb_hid
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
import adafruit_ducky
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
num_modules = len(sys.modules)
print(f"[*] Imported {num_modules} Modules [{execution_time}ms]")

start_time = time.monotonic()
led_pin = board.LED
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
print(f"[*] Setup LED [{execution_time}ms]")

start_time = time.monotonic()
button = DigitalInOut(board.BUTTON)
button.direction = Direction.INPUT
button.pull = Pull.UP
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
print(f"[*] Setup BUTTON [{execution_time}ms]")

start_time = time.monotonic()
time.sleep(1)
keyboard = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(keyboard)
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
print(f"[*] Setup KEYBOARD [{execution_time}ms]")

start_time = time.monotonic()
payload_path = "payload.txt"
duck = adafruit_ducky.Ducky(payload_path, keyboard, keyboard_layout)
with open(payload_path, 'rb') as payload:
    payload.seek(0, 2)
    payload_size = payload.tell()
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
print(f"[*] Loaded Payload. [{payload_path}] [{payload_size}B] [{execution_time}ms]")

def execute():
    result = True
    while result is not False:
        result = duck.loop()

print("[*] Awaiting Button Press...")
while True:
    if not button.value:
        time.sleep(0.1)
        if not button.value:
            start_time = time.monotonic()
            print("[*] Executing Payload...")
            led.value = True
            execute()
            led.value = False
            end_time = time.monotonic()
            execution_time = (end_time - start_time) * 1000
            print(f"[*] Executed Payload [{execution_time}ms]")
            while not button.value:
                pass
    time.sleep(0.01)