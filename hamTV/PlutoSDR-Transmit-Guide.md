## Transmitting DVB-S2 Via Adalm Pluto SDR
* Ubuntu 22.04
* 2 options
  * local install 
  * docker container install (preferred + more setup)

### Pluto Drivers
* run `sudo apt-get install libiio-utils`
* restart your machine
* if the pluto is detected as a mass storage device, this was successful

### Installing Transmit Software
* using simple CLI app [gr-dvbs2rx](https://github.com/igorauad/gr-dvbs2rx) by igorauad
* Very easy to use, very well documented software. Installation instructions [here](https://github.com/igorauad/gr-dvbs2rx/blob/master/docs/installation.md). 
* Usage instructions [here](https://github.com/igorauad/gr-dvbs2rx/blob/master/docs/usage.md)

### Testing transmit software
* install [TSDuck](https://tsduck.io/download/tsduck/)
  * allows for automatic generation of test transport stream files
  * run using `tsp`
* run the command `tsp -I craft --pid 100 | dvbs2-tx | dvbs2-rx`. You should see a big wall of characters. This means its working

### Running Transmit Software with Pluto Sink
* requires you create a transport stream (.ts) file
* run the command `cat filename.ts | dvbs2-tx --sink plutosdr --freq *frequency-in-MHz*M --sym-rate *symbol-rate* --modcod QPSK1/2`. This will start the dvbs2 transmission
* modcod sets the modulation and FEC. In this case QPSK and 1/2 FEC

### Receiving Transmitted Signal
* tested with BATC Minitiouner software
* configure all settings to match transmit characteristics
* ensure codec is set to H264
* known to not work well with sdrangel and rtl-sdr

