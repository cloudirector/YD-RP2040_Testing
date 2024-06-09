<div align="center">
<p align="center">
  <img src="https://github.com/cloudirector/YD-RP2040_Testing/assets/143876484/39c3627d-cc5d-40f8-8189-01c27c38cbeb" width="50%" height="50%">
</p>
  
# YD-RP2040_Testing <br>
This is a CircuitPython testing repo for the YD-RP2040.
  
</div>

### The Firmware used on my board

* [CircuitPython Version for My Board](https://circuitpython.org/board/vcc_gnd_yd_rp2040)

### The Board

* [Here it is on Aliexpress](https://www.aliexpress.us/item/3256803817805852.html)

### Tools Used

* [minicom](https://wiki.emacinc.com/wiki/Getting_Started_With_Minicom)
* [circup](https://github.com/adafruit/circup)

<div align="center">
  
# Setup <br>
(read this)
  
</div>

#### Factory Reset Board (recommended, but "you do you").

##### Put into bootloader mode

1. Press and release the Reset button.
2. Continue holding the Boot button until you see the RPI-RP2 drive appear on your computer.
3. You can now release the Boot button.

##### Upload the reset firmware(s).

1. [Download factory reset firmware](https://github.com/adafruit/Adafruit-Feather-RP2040-RFM-PCB/raw/main/factory-reset/feather-rp2040-rfm69-factory-reset.uf2) into or put it into the drive that appeared.
   * Side note: if your board is str8 messed beyond your fancy... [Download this firmware instead](https://cdn-learn.adafruit.com/assets/assets/000/101/659/original/flash_nuke.uf2) to nuke the stuff out of its Flash.

#### Installing CircuitPython (again recommended, but if you have better firmware or a legit board, this step is not required.)

1. [Download the firmware](https://downloads.circuitpython.org/bin/vcc_gnd_yd_rp2040/en_US/adafruit-circuitpython-vcc_gnd_yd_rp2040-en_US-9.0.5.uf2) into or put it into the drive that appears with fresh firmware.
2. Wait for its epic uf2 magic to finish ;)
3. This step is optional but it may be what you need, unplug that and replug that simple as it is.

#### Upload the code

One way is to Navigate to the drive's directory once your device is not in bootloading mode in your shell and git clone this repo;

```git clone https://github.com/cloudirector/YD-RP2040_Testing```

You can also just [Download the repo](https://github.com/cloudirector/fcnc/archive/refs/heads/main.zip) and extract to the drive.

#

<div align="center">
  
# Usage <br>
(Not yet Completed.)
  
</div>

Click Button Once to start a session.

Once in Session the light should be blinking.

Click and hold on the blue first module, hold on the blank second module.
