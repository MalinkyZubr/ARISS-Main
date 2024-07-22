from gpiozero import LED
from time import sleep
from typing import Callable

    
def extract_callsign_binary(callsign_path: str) -> str:
    try:
        file = open(callsign_path)
        callsign: str = file.readline().split(" ")[0]
    except:
        callsign: str = "AMSAT"

    binary_callsign: str = ''.join(format(ord(i), '08b') for i in callsign)

    return binary_callsign

def low(led: LED) -> None:
    led.off()
    sleep(0.25)

def dot(led: LED) -> None:
    led.on()
    sleep(0.25)
    low(led)

def dash(led: LED) -> None:
    led.on()
    sleep(0.5)
    low(led)

def morse_function_generator(binary_callsign: str) -> list[Callable]:
    morse_function: list[Callable] = []
    for bit in binary_callsign:
        if bit == "0":
            morse_function.append(dot)
        else:
            morse_function.append(dash)
    
    return morse_function

def run_morse_function(function: list[Callable], led: LED) -> None:
    for bit_action in function:
        bit_action(led)


if __name__ == "__main__":
    led: LED = LED(21)
    binary_callsign: str = extract_callsign_binary(r"/home/pi/CubeSatSim/sim.cfg")
    morse_function: list[Callable] = morse_function_generator(binary_callsign)

    while True:
        run_morse_function(morse_function, led)