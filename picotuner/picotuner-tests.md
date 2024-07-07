# Picotuner Tests
* These tests are conducted to identify the optimal software configuration of the PicoTuner receiver board, and confirm functionality when operating alongside several different transmitters

## Test Transmitters
- all transmitters use DVB-S modulation, at a distance of 1/2 meters
* #### BATC Rapsberry Pi Ugly DATV transmit
  * very simple transmitter for still image. High frequency bit bashing on GPIO pin to emulate antenna. Operates over very short range
* #### Digilite-ZL
  * transmitter test source playing looped video 
* #### Adalm PlutoSDR
  * educational tool capable of transmitting DVB-S 
  * transmitted using DATV-express [here](https://datv-express.com/wp-content/uploads/2022/08/Windows_setup_datvexpress_dvb_transmitter_v1.25LP14.7z)
    * ##### configuration: (all settings not mentioned left at default)
      - Modulator
        - Common
          - TX Frequency: 2 ghz
          - TX Symbol Rate: 333 kS/S
          - SDR HW: Pluto
        - DVB-S
          - FEC: 1/2
      - Options
        - On Air Format
          - Transmitted Format: 640 480 15
      - Codec
        - Video
          - H.264
          - Performance: Fast
    * ##### Operation
      * to transmit, just click PTT button to save configure. Click again to begin transmission
    * ##### Known Issues
      * Incompatible with windows 11
        * crashes when transmitting with video source
      * transmission cutout
        * lower end/less powerful host hardware
        * exceeding 1000 kS/S sample rate (with mmpeg2), or using H.265 video codec
        * transmission will periodically cut out if the host has to work too hard. Lock impossible

## Environment Setup
### Opentuner receiver
Installation steps for setting up picotuner on rpi pico (using windows)
* driver install
  * install Zadig [here](https://zadig.akeo.ie/)
  * open zadig -> options -> list all devices
  * dropdown menu, install batc picotuner TS interfaces 0 AND 1

#### Firmware Setup
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