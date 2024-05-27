Installation steps for setting up picotuner on rpi pico (using windows)
1. Download the picotuner test program [here](https://www.dropbox.com/scl/fi/3ziiiq71hretd2yzaou8f/picotuner_driver_test_app.zip?rlkey=gl4xsxddxprxfvjjydebvez5y&e=1&dl=0)
   1. run the tester exe as administrator
   2. hit "install drivers"
2. Download the [picotuner uf2 file](https://github.com/g4eml/PicoTuner/releases/download/v0.11-alpha/PicoTunerV0-11.uf2)
   1. while holding the BOOTSEL button on rpi pico, plug into host via micro-usb. (this should mount the pico as an external drive)
   2. copy the uf2 file to the pico, the driver should unmount, and the LED on the pico should blink.
   3. in the picotuner tester, click 'Detect Device/Drivers' (there should be no errors)
3. Install open tuner for windows
   1. download the opentuner zip file [here](https://www.zr6tg.co.za/files/open_tuner_0.A.zip)
   2. run the exe enclosed
   3. rpi pico should interface properly with the software

### Sources:
* https://www.zr6tg.co.za/open-tuner/
* https://wiki.batc.org.uk/PicoTuner
* https://www.zr6tg.co.za/2024/02/11/picotuner-an-experimental-dual-ts-alternative/
