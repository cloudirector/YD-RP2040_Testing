print(f"[*] Importing Modules...")
import time
start_time = time.monotonic()
import sys
import usb_hid
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
from hashing import *

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

hash_count = 1000
def execute():
    for nonce in range(hash_count):
        start_time = time.monotonic()
        hashed_nonce = sha256(str(nonce))
        end_time = time.monotonic()
        execution_time = (end_time - start_time) * 1000
        print(f"{nonce}:{hashed_nonce} [{execution_time}]")

print("[*] Awaiting Button Press...")
while True:
    if not button.value:
        time.sleep(0.1)
        if not button.value:
            start_time = time.monotonic()
            print("[*] Running Test With {hash_count} nonces...")
            led.value = True
            execute()
            led.value = False
            end_time = time.monotonic()
            execution_time = (end_time - start_time) * 1000
            print(f"[*] Finished Test [{execution_time}ms]")
            while not button.value:
                pass
    time.sleep(0.01)