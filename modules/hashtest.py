print(f"[*]     Importing HashTest Modules...")
import time
start_time = time.monotonic()

import os
import sys
import board
import digitalio
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from modules.functions.hashing import *
end_time = time.monotonic()
execution_time = (end_time - start_time) * 1000
num_modules = len(sys.modules)
print(f"[*]     Imported {num_modules} Modules [{execution_time}ms]")

def hashtest(nonces):
    wrapper_start_time = time.monotonic()
    print("[*] Running HashTest With {nonces} nonces...")
    for nonce in range(nonces):
        start_time = time.monotonic()
        hashed_nonce = sha256(str(nonce))
        end_time = time.monotonic()
        execution_time = (end_time - start_time) * 1000
        print(f"[*] [{nonce}:{hashed_nonce}] [{execution_time}]")
    end_time = time.monotonic()
    execution_time = (end_time - wrapper_start_time) * 1000
    print(f"[*] Finished Test [{execution_time}ms] [{nonces / (execution_time / 1000)} h/s]")