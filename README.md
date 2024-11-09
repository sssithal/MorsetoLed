Morse Code LED Blinker

This project uses the Raspberry Pi's GPIO pins to blink an LED in Morse code for any given message. The program takes a message and a number of repetitions as input and blinks the LED in the corresponding Morse code pattern.

Requirements:

    Hardware: Raspberry Pi with an LED connected to GPIO pin 17 (BCM numbering).
    Python 3
    RPi.GPIO library (for controlling GPIO pins)

Installing RPi.GPIO

To install the RPi.GPIO library, use:

pip install RPi.GPIO

Wiring

Connect an LED to GPIO 17 (physical pin 11) on the Raspberry Pi, with the appropriate resistor in series to limit current.
Usage:

    Run the Script: Use the command below to send a message in Morse code via the LED.

python3 send.py <repetitions> <message>

    <repetitions>: Number of times to repeat the message.
    <message>: The message to convert to Morse code (letters, numbers, and spaces only).

Example: To blink "HELLO" three times:

    python3 send.py 3 "HELLO"

Morse Code Timing

    Dot: 0.2 seconds (adjustable)
    Dash: 3x dot duration
    Letter space: 3x dot duration
    Word space: 7x dot duration

Code Explanation

    Morse Code Dictionary: Converts letters and numbers to Morse code.
    Functions:
        blink_dot(): Lights the LED for a dot duration.
        blink_dash(): Lights the LED for a dash duration (3x dot duration).
        send_morse_code(message, repetitions): Blinks each character of the message in Morse code for the specified repetitions.

Cleanup

The GPIO.cleanup() function ensures that GPIO resources are properly released after the program ends.


    
