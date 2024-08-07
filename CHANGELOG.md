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
* setup FoxTelemetry decoder alongside rtl-sdr and assembled cubesatsim to receive simulated cubesat telemetry
  * attempted with virtual audio cables integrated with SDRpp as well as on linux with rtl_fm and multimon-ng, however these proved (for now) to be nonfunctional

06/27/2024 - 9 am - 5 pm independent work
* Coordinated with caden peters to write blurb for magazine publication
* identified 3 test setups for cubesat
* installed and attempted configuration of 3 cubesat receive test softwares
* identified 3 picotuner tests, setup test result spreadsheets
* installed datvexpress software and began running tests of the plutosdr as a test transmitter for picotuner
* began formalizing test instructions for picotuner and cubesatsim
* learned about dc offset and IQ imbalancing

06/28/2025 8am - 5pm independent work
* operational amplifier design
* conductance angle, amplifier classes, importance of different stages and biasing, importance of recovery for BJTs in amplifiers
* inactive vs active periods on amp
* BJT regions of operation, amplifier clipping due to saturation
* darlington transistors and their value

07/01/2024 9 am - 6 pm independent work
* weekly briefing meeting
* bowersox talk
* ham radio studying
* built 2.4 ghz ground plane antenna
* 1 on 1 meeting with Korine Powers
* continued troubleshooting crashing issues with OpenTuner, contacted primary developer on github for assistance
* continued to attempt to get the plutosdr transmit to work. Working through consistent crashing issues with DATV express on windows. Attempted and failed wine installation on linux
* began studying linear DC circuit design
* received ST2 programmer, began programming vaisala rs41
  * will figure this out later
  * read more about different modes, mode change button
  * see pictures for more info
* got to work with plutosdr driver installs and DATVExpress
* get the DVB-s express for plutosdr
* sync with caden to begin work on the magazine article
* signal splitter
* planned for week's activities, next meeting, learn about ground plane antennas
* learn about the dc spike, IQ imbalancing

07/02/2024 9am - 5 pm 45 mile drive
* learn about buck converters
* planning for satellite tracking rotator system to use with picotuner receive
* discussed and planned possibility of desinging in house MCU based rotator system
* attended lecture of how to make most of internship
* reed relay coil
* confirmed that datvexpress works in windows 10, plan to setup windows 10 vm in future for proper function, with both mpeg2 and h264. h265 too much for kerry laptop
* identified successful operation of opentuner on a desktop computer running windows 10. Will try building opentuner from source to avoid machine specific problems with precompiled binaries.

07/03/2024 9am - 6 pm independent work:
* attended weekly standup meeting
* attended catchup meeting with Pete to coordinate construction of picotuner
* successfully ran DATV-Express on microcomputer, transmission with pluto with no crash, failed to receive due to inconsistent transmission
* attempted manual installation and operation of QSSTV on linux
* Chose to install the ground station OS card to a raspberry pi (all test software for cubesatsim preinstalled)05/24/24 3pm - 6:45 pm, 80 miles drive
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
* setup FoxTelemetry decoder alongside rtl-sdr and assembled cubesatsim to receive simulated cubesat telemetry
  * attempted with virtual audio cables integrated with SDRpp as well as on linux with rtl_fm and multimon-ng, however these proved (for now) to be nonfunctional

06/27/2024 - 9 am - 5 pm independent work
* Coordinated with caden peters to write blurb for magazine publication
* identified 3 test setups for cubesat
* installed and attempted configuration of 3 cubesat receive test softwares
* identified 3 picotuner tests, setup test result spreadsheets
* installed datvexpress software and began running tests of the plutosdr as a test transmitter for picotuner
* began formalizing test instructions for picotuner and cubesatsim
* learned about dc offset and IQ imbalancing

06/28/2025 8am - 5pm independent work
* operational amplifier design
* conductance angle, amplifier classes, importance of different stages and biasing, importance of recovery for BJTs in amplifiers
* inactive vs active periods on amp
* BJT regions of operation, amplifier clipping due to saturation
* darlington transistors and their value

07/01/2024 9 am - 6 pm independent work
* weekly briefing meeting
* bowersox talk
* ham radio studying
* built 2.4 ghz ground plane antenna
* 1 on 1 meeting with Korine Powers
* continued troubleshooting crashing issues with OpenTuner, contacted primary developer on github for assistance
* continued to attempt to get the plutosdr transmit to work. Working through consistent crashing issues with DATV express on windows. Attempted and failed wine installation on linux
* began studying linear DC circuit design
* received ST2 programmer, began programming vaisala rs41
  * will figure this out later
  * read more about different modes, mode change button
  * see pictures for more info
* got to work with plutosdr driver installs and DATVExpress
* get the DVB-s express for plutosdr
* sync with caden to begin work on the magazine article
* signal splitter
* planned for week's activities, next meeting, learn about ground plane antennas
* learn about the dc spike, IQ imbalancing

07/02/2024 9am - 5 pm 45 mile drive
* learn about buck converters
* planning for satellite tracking rotator system to use with picotuner receive
* discussed and planned possibility of desinging in house MCU based rotator system
* attended lecture of how to make most of internship
* reed relay coil
* confirmed that datvexpress works in windows 10, plan to setup windows 10 vm in future for proper function, with both mpeg2 and h264. h265 too much for kerry laptop
* identified successful operation of opentuner on a desktop computer running windows 10. Will try building opentuner from source to avoid machine specific problems with precompiled binaries.
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
* setup FoxTelemetry decoder alongside rtl-sdr and assembled cubesatsim to receive simulated cubesat telemetry
  * attempted with virtual audio cables integrated with SDRpp as well as on linux with rtl_fm and multimon-ng, however these proved (for now) to be nonfunctional

06/27/2024 - 9 am - 5 pm independent work
* Coordinated with caden peters to write blurb for magazine publication
* identified 3 test setups for cubesat
* installed and attempted configuration of 3 cubesat receive test softwares
* identified 3 picotuner tests, setup test result spreadsheets
* installed datvexpress software and began running tests of the plutosdr as a test transmitter for picotuner
* began formalizing test instructions for picotuner and cubesatsim
* learned about dc offset and IQ imbalancing

06/28/2025 8am - 5pm independent work
* operational amplifier design
* conductance angle, amplifier classes, importance of different stages and biasing, importance of recovery for BJTs in amplifiers
* inactive vs active periods on amp
* BJT regions of operation, amplifier clipping due to saturation
* darlington transistors and their value

07/01/2024 9 am - 6 pm independent work
* weekly briefing meeting
* bowersox talk
* ham radio studying
* built 2.4 ghz ground plane antenna
* 1 on 1 meeting with Korine Powers
* continued troubleshooting crashing issues with OpenTuner, contacted primary developer on github for assistance
* continued to attempt to get the plutosdr transmit to work. Working through consistent crashing issues with DATV express on windows. Attempted and failed wine installation on linux
* began studying linear DC circuit design
* received ST2 programmer, began programming vaisala rs41
* read dave israel papers on DSN
* give kate oberlander RObert contact for her sister, urban design
  * koberlander@g.ucla.edu
* read dave israel papers on DSN
* give kate oberlander RObert contact for her sister, urban design
  * koberlander@g.ucla.edu
  * will figure this out later
  * read more about different modes, mode change button
  * see pictures for more info
* got to work with plutosdr driver installs and DATVExpress
* get the DVB-s express for plutosdr
* sync with caden to begin work on the magazine article
* signal splitter
* planned for week's activities, next meeting, learn about ground plane antennas
* learn about the dc spike, IQ imbalancing

07/02/2024 9am - 5 pm 45 mile drive
* learn about buck converters
* planning for satellite tracking rotator system to use with picotuner receive
* discussed and planned possibility of desinging in house MCU based rotator system
* attended lecture of how to make most of internship
* reed relay coil
* crystal radio learning, half wave rectifier diode
* meet and greet meeting with nasa folks
* learned about crystal radio, will build one
* learned about grounding of antennas, parasitic capacitances, ground plane function
* find another antenna to make

07/03/2024 9am-5pm independent work
* worked on compiling opentuner from source
* configured and setup raspberry pi 3 ground station for the cubesatsim
* updated test documentation
* met with randy berger and pete to sync on the construction of picotuner and share experiences
* began researching design principles of dipole antennas and the yagi uda antenna

07/05/2024 9am - 5pm independent work
* began initial brainstorming on MCU sun rotator system
* read paper on DSN by dave israel
* began construction of Yagi Antenna

07/08/2024 9am - 5pm 45 mile drive
* cut additional boards for cubesatsim
* soldered additional raspberry pis for cubesatsim
* flashed additional cubesatsim SD cards
* attended weekly briefing meeting
* got QSSTV to work with cubesatsim using audio cable between two laptops. WIll make the virtual interface work later
* installed the fldigi morse decoder, observed morse mode for cubesat on sdrpp

07/09/2024 9am - 5pm independent work
* continued testing and calibration of yagi antenna
* set up meeting with dave israel
* met with dave israel
* worked on final presentation with caden
* got access to updated version of opentuner, setting up test transmitter, gnuradio,uglydatv 
* nstalled and set up kicad on desktop environment
* began development of kicad schematic for cubesatsim

07/10/2024 8:30 am - 5pm independent work
* extensive reading into AM modulation design and mathematics
* reading into the design and operation of class B amplifiers
* binary power supplies and DC biasing
* read IOAG recommendations on selection of BP or IP paper

07/11/2024 8am - 5pm independent work
* built example AM modulation script in gnu radio
* continued setup of gnuradio with pluto
  * successfully made test NBFM transmission with pluto 
* finished and submitted first iteration of KiCad schematic to Kerry
* contributed edits to the team magazine publication thing
* contributed to final presentation for internship end

07/12/2024 9am - 5pm independent work
* weekly meeting with intern fellows
* began design for cmos based virtual interrupt expander for arduino uno
* began looking into RGB arrays via I2C for arduino
* continued learning about electronics

07/15/2024 9am - 7 pm 45 mile drive
* finished assembly of 2 additional cubesat sim units
  * soldering of radio boards
  * increasing tolerance of 3d printed parts
  * assembly of LED arrays
* tested new version of OpenTuner, confirmed functionality
* observed radio calibration/signal strength testing
* discussed KiCad design, communicated with coworkers about design for pi sensor hat
* attended weekly briefing
* completed yagi antenna design

07/16/2024 9am - 5 pm independent work
* worked heavily on final presentation powerpoint
* powerpoint practice run
* received and implemented KiCad feedback from thompson. Returned all questions he had

07/17/2024 9am -5pm independent work
* continued working on implementing powerpoint feedback
* continued designing code to help with boolean algebra in digital circuits
  * multisim for encoder
* soldered adapters for cubesatsim LEDs
* sscheduled pee review for presentation

07/18/2024 9am-5pm independent work
* Watched video describing operation of switching power supplies
* standup meeting
* tracked SAT pirates from brazil using homemade yagi
* assembled standoffs for cubesatsim system
* continued testing with DATVExpress on multiople machines
* tested cubesatsim boxes

07/19/2024 9am-5pm independent work
* attended weekly catchup meeting
* began repairs on cubesatsim tops
* began work on LED blinker program for the cubesatsim
* developed library for interrupt expander

07/22/2024 9am-5pm independent work
* completed repairs on one cubesatsim top
* finished development of morse code blinker for cubesatsim
  * necessitated ISO extraction for source files in system
* attended weekly briefing

07/23/2024 9am-5pm independent work
* setup for ham radio exam
* purchased USB adapter for raspberry pi 0 to upload code
* continued library implementation for the interrupt expander
* began research into quine method for boolean reduction
* continued working on setting up gnuradio for pluto
* writing script for presentation

07/24/2024 9am-6pm independent work
* developed full quine algorithm program
* improved design of sensor hat PCB to reduce footprint and improve airflow
* set up for printing of PCB boards for sensor hat
* received and began assembly of Yagi tripod mount
* continued efforts to transmit plutosdr dvb-s

07/25/2024 9am-5pm independent work
* peer review session for presentation
* continued working on improving presentation script, implementing advice
* continued deevelopment of interrupt expander
* reading the bundle protocol specification
* research into low power microcontrollers for parallel to serial conversion and communication management
* finally made successful dvb-s transmission with pluto, briefly. Posted issue to software github

07/26/2024 9am-5pm
* weekly intern catchup session
* developing C library for interrupt dxpander
* research into TWI serial communication protocol for ATiny85 microcontroller
* circuit design in multisim for 32-5 encoder using improved, simplified boolean expression
* experimenting with hardware interrupts on the arduino
* imploementing interrupt debouncing in hardware for arduino

07/29/2024 9am-5pm 45 mile drive
* weekly briefing
* successfully received dvb-s with the picotuner
* planned for dress rehearsal with kerry and randy
* test setup with plutosdr and successful DVB-s transmit
* installed LEDs on cubesatsim boards
* wrote up guide on transmitting dvb-s2 on adalm pluto
* further picotuner testing, submitted new issue
