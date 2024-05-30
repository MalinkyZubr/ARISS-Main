# HamTV
* use AM or VSB vestigal sideband
* 2 m band, 6 mhz bandwidth too small
* video and audio on different frequ8encies
* hamtv signals weak, pre-amplifier needed in many cases to ensure reception
* fm used on higher frequency, needs separate demodulator

### Preamplifier
* amplify raw signal to make sure signal processing can be completed
* must be strong enough to ensure noise tolerance during processing.
* must be places close to antenna to reduce noise
* high input impedance (detect), low output impedance (low voltage drop with current consuming load)
* ideally does not add noise, or decrease signal to noise ratio (LNA)


### FM HamTV
* above 1.24 Ghz (enough bandwidth for wideband)
* VSB used, figure out what this is


### P levels
* measurement of image quality, based on test pattern
* each level represent 6 dB increase, starting at 0 dB.
* 5 levels, 1 to 5


### SHF
* super high frequency
* loss due to atmosphere, structures, hills
* no atmosphere bouncing


### STB
* receive lower frequency commercial channels
* lower frequencies better for coax
* needs LNB for frequency downconversion.
* cannot tune high enough to receive hamtv, need special downconverter to do this
* dvb-t

## notes
* frontent of receiver: connect to antenna
* local oscillator determine frequency range. LO and mixer are setp before ADC
* learn about timing averaging signal boost thing
* learn viterbi9
* learn I and Q
* rtl sdr block diagrams
* sdrpp tutorial
https://www.amsat-on.be/hamtv-summary/ariss-ham-tv/
* swr, standing wave ratio, learn
* read up on fec
* read polarized antennas, multiple signals safe frequency, circular polarization
https://forum.amsat-dl.org/index.php?thread/3931-helix-tx-antenna-is-this-good-to-go/

* learn about phase lock loop
* doppler shifting
* hackrf
* sdr angel (hamtv capable, with hackrf, demod tv, dvb-s)
* LimeSDR
* srdangel video
* HAM license
* free DV on raspberry i
* m17 project
* phil karn SW ka9q-radio
* cosmic watch
* ultrasonic microphone fft
  * muons, cosmic rays
* qpsk, bpsk
* 