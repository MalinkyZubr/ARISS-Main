05/24/24 3pm - 6:45 pm, 80 miles drive
* Project/personal introductions
* basic roadmapping
* Soldered rpi pico and header pins to the PicoTuner board

05/27/2024 9:15 am - 2:30 pm, 60 miles drive
* installed open-tuner software to windows boot
* installed USB drivers using the picotuner test script
* flashed rpi pico with PicoTuner uf2 file
* setup and ran minitiouner software with Digilite \ZL Ariss test signal transmitter
* do decibel calcs
* minitiouner setup and installation complete, successfully receive test signal
* did the talking and study about the weather balloons
* learned about operating CW signals

05/28/2024 10 am - 5 pm 45 miles drive
* read basics on wikipedia about hamtv
* overviewed ARISS hamtv funcitonality
* introduction to SDR++, radio concepts
* got some new materials to read about antennas, and math
* set up sdrangel with hackrf and rtl-sdr
* overviewed the superheterodyne block diagram
* USB and LSB distinction, reasoning

5/30/2024 10:30 am - 45 miles drive
* portsdown 2020 ugly datv
* hackrf 2020 portdown ugly datv
* minitiouner receive ugly datv portsdown
* sync on project goals prior to official start date
* tested portdown ugly datv with open tuner software
* successfully transmitted test pattern with hackrf using sdrangel
* relationship between signal power, bandwidth

5/31/2024 - indepentent work at home
* learned about importane of impedance
* learned about the danger of reflection in RF circuits due to poor impedance matching
* learned impedance matching circuits/networks
* learned about image rejection, how it relates to mixer, and how it is dealt with
* got the skywatch to work

6/1/2024 - independent work at home
* began studying for the ARRL ham radio technician license test
* set up test equipment at home, preparing for use

6/3/2024 - independent work at home, 6:30 am - 5 pm
* orientation meeting
* first SIP standup
* learned about the 'DC Spike', and why it occurs
* configuring noolec sdr smart for linux
* research into vaisala rs41 radiosconde telemetry
* research into gfsk, radiosconde operations
* intersymbol interference
  * multipath propogation
  * bandlimited channels
* PSK and its relationship to the complex plane (data encoded in complex plane)
* ADC design, sample rate vs conversion rate, ADC resolution/sensitivity

6/4/2024 - independent work 9 am - 5 pm
* extensive reading of pyrtlsdr when developing test demonstration for dongle
* investigation of USB operations and DVB-s demodulation in opentuner software
* brainstorming on more user friendly software for DVB-S reception that may be more conducive for simple communication
* brainstorming on webSDR for retransmitting DVB-S to the itnernet

6/5/2024 - independent work 7:30 am - 5:45 pm
* studying for ham radio technician exam
* finished configuring laptop for use in work
* read academic article, "What nyquist didnt say"
* began preliminary development of crude fm radio receiver using pyrtlsdr
* learned about DC frequency and FFTshift
* learned about spectral density graph

6/7/2024 -independent work 8:30 am - 
* read about FEC error correction, and encoding techniques
* read about DSP, hilber transformation, amplitude loss on mixing
* 2 hours review on complex number operations and uses
* continued working on pyrtlsdr development work

6/10/2024 - independent work 9 am - 6 pm
* set up windows development environment to begin fork of opentuner
* began examining opentuner source code in greater detail
* learned about RIT (radio incremental tuning)
* read in book on operations of BJT transistors
* assembled simple single stage amplifier with BJT, experimented with different configurations
* installed and confiugred wine for linux to run LTSpice


6/11/2024 - 9 am - 5 pm, 45 miles drive
* began assembly of the picotuner board
* completed on the wire meeting
* REMEMBER:
  * assemble list of contacts spreadsheet
  * make it known I want to come back for full time or another internship

6/12/2024 - 10 am - 5 pm 45 miles drive
* finished assembly of the picotuner board
* successfully tested the picotuner with the datv-ugly and the Digilite-Zl
* assembled the picotuner encasement box using drill press

6/13/2024 - 11 am - 5 pm independent work
* carsons rule (bandwidth = 2 * sum highest modulating frequency & deviation) for fm
* meteor scatter
* CTCSS tones for opening repeaters
* reading about capacitive reactance, kirchoffs laws, AC circuits
* APRS Automatic packet reporting system
* ARQ Automatic repeat request
* NET control stations
* PTT push to talk

06/14/2024 - 9am - 5pm 45 miles drive
* meeting with Randy and co
* REMEMBER:
  * prepare for presentation wiht the BATC people to present work with picotuner
* generated labels for picotuner case
* ran antenna tests for picotuner at longer range
* troubleshooted compatability issues between picotuner and windows 11 VLC (hardware deecoding)
* continued studying for the ham radio test

06/17/2024 - 7:30 am - 5:30 pm - independent work
* meeting with leadership
* sip weekly briefing
* read extensively into filter operations and design, especially focusing on resonant circuits, bandwidth, center frequency, etc
* learned how to use bode plotter
* explored harmonics of RF signals, how this relates to amplification and other operations, connected this to the PLL
* set up multisim with shared folders in virtual machine to allow for easy testing of rf circuits
* made ohms law calculations using ohms law of reactance, vectorized view of reactance and

06/18/2024 - 9 am - 5 pm - 45 miles drive
* Continued detailed exploration of RC and RL circuits in application to analog filters
* understood frequency response difference between bandstop parallel resonant filter and bandpass series resonant filter
* explored the concepts of feedback as it has to do with operational amplifiers
* operational amplifier archtiecture, constituent parts of op-amp
  * both positive and negative terminals should try and remain the same. Amp drives harder or lower to compensate for voltage changes
* 3 terminal variable voltage/current regulator circuits
* voltage referencing in op-amps, bandgap reference
* experimented using the BATC portsdown4 platform to drive the picotuner/minitiouner boards
  * identified issues setting center and LNB frequencies (to ask the batc people)
* gained familiarity with ltspice
* set up ssh on the cubesat simulator
* milled and cut copper board for cubesat simulator
* glued/attached standoff spacers to cubesat body for attaching of rpi zero-w
* soldered replaced OLED board for damaged cosmic watch
  * tested all cosmic watches, identified light leakage in one of them

06/24/2024 - 9 am - 5 pm 45 miles drive
* cubesatsim assembled with radio hat, successfully transmit and receive telemetry
  * 434.013 MHz identified as true frequency
* setup FoxDecode decoder alongside rtl-sdr and assembled cubesatsim to receive simulated cubesat telemetry
  * attempted with virtual audio cables integrated with SDRpp as well as on linux with rtl_fm and multimon-ng, however these proved (for now) to be nonfunctional
* 