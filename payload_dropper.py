import time
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.keycode import Keycode
import usb_hid

led_pin = board.LED
led = digitalio.DigitalInOut(led_pin)
led.direction = digitalio.Direction.OUTPUT

kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayoutUS(kbd)

button = DigitalInOut(board.BUTTON)
button.direction = Direction.INPUT
button.pull = Pull.UP

def blink(interval, blinks):
    for i in range(blinks):
        led.value = True
        time.sleep(interval)
        led.value = False
        time.sleep(interval)

def type(string):
    layout.write(string)

payload_path = "payload.txt"

with open(payload_path, 'r') as file:
    payload = file.read()

while True:
    if not button.value:
        time.sleep(0.1)
        if not button.value:
            led.value = True
            type(payload)
            led.value = False
            while not button.value:
                pass
    time.sleep(0.01)