print(f"\n[*] Importing Main Modules...")
import time
start_time = time.monotonic()

import os
import sys
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull

from modules.rubberducky import rubberducky
from modules.hashtest import hashtest

end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
num_modules = len(sys.modules)
print(f"[*] Imported {num_modules} Main Modules [{execution_time}ms]")

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

print("[*] Awaiting Button Press...")
while True:
    if not button.value:
        time.sleep(0.1)
        if not button.value:
            start_time = time.monotonic()
            print("[*] Started Session")
            led.value = True
            while True:
                time.sleep(2)

                led.value = True
                if not button.value:
                    print("[*] Awaiting Button Press...")
                    while True:
                        if not button.value:
                            time.sleep(0.1)
                            if not button.value:
                                start_time = time.monotonic()
                                hashtest(100)
                                end_time = time.monotonic()
                                execution_time = (end_time - start_time) * 1000
                                while not button.value:
                                    pass
                                break
                        time.sleep(0.01)
                    break

                time.sleep(1)

                led.value = False
                if not button.value:
                    print("[*] Awaiting Button Press...")
                    while True:
                        if not button.value:
                            time.sleep(0.1)
                            if not button.value:
                                start_time = time.monotonic()
                                rubberducky("files/payload.txt")
                                end_time = time.monotonic()
                                execution_time = (end_time - start_time) * 1000
                                while not button.value:
                                    pass
                                break
                        time.sleep(0.01)
                    break

            led.value = False
            end_time = time.monotonic()
            execution_time = (end_time - start_time) * 1000
            print(f"[*] Breaking Session [{execution_time}ms]")
            while not button.value:
                pass
    time.sleep(0.01) 
    # type: ignore