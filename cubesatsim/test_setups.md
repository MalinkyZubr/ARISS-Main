# Cubesatsim test setups
https://cubesatsim.org/download/cubesatsim-lite-readme.pdf

### Parameters
* goal of these tests is to ensure proper function of cubesatsim telemetry transmission
* compare ease of use between different software stacks and their respective modes of operation
* compare ease of use between different hardware stacks/test with different receivers

### Modes of Operation 
1. APRS -> SoundModem/Direwolf (windows) | OpenWebRX/Direwolf (linux + spreadsheet)
2. FSK -> FoxTelem
3. BPSK -> FoxTelem
4. SSTV -> Windows MMSSTV / Linux QSSTV
5. CW -> fldigi with spreadsheet

### receivers to test
* PlutoSDR
* Nooelec Nesdr Smart
* RTL-SDR

### Mode Change Test
* pressing and holding the "mode change" button will switch modes. 
#### To Select mode
1. hold the mode change button
2. watch the power LED. It should blink
3. Count the number of times the LED blinks in sequence. Releasing the button at this point will select the mode of the matching number
4. wait about 20 seconds, will begin transmitting in new mode. Transmission starts with short morse code message

#### Test Results
* Some mode changes caused frequency shift of a few kHz
* all modes successfully transmit as described in documentation

##### Software Stacks (APRS + Linux)
* rtl_fm + multimon-ng
  * was not able to decode anything consistently with multimon-ng. Very limited documentation
  * rtl_fm receives fine
  * inconvenient to use, will investigate more later
* OpenWebRX (installed at https://www.openwebrx.de/download/ubuntu.php)
  * was able to receive signals from the cubesatsim
  * low degree of flexibility/configurability. Many steps to set up web service
    1. install from website
    2. create admin account at setup
    3. go to /etc/openwebrx to configure port in openwebrx.conf
    4. login on localhost at specified port with the admin account made earlier
    5. create a new receive profile for desired frequencies (parameters like center frequency, sample rate, etc. During operation you only have access to frequencies that are delineated in the profile)
    6. setup decoding in the browser for packet signals
  * would be useful, as stated in documentation (https://cubesatsim.com/content/CubeSatSimPaper4.pdf) for classroom activities where "up to twenty users" need to access and decode telemetry separately

##### Software Stacks (FSK + Linux/Windows)
* FoxTelem
  * http://amsat.us/FoxTelem
  * very simple and easy install both on linux and windows
  * works out of the box for FSK feeding directly from an RTL-SDR dongle. Decodes and formats telemtry data