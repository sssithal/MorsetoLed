import RPi.GPIO as GPIO
import time
import sys

# Define the GPIO pin where the LED is connected
LED_PIN = 17  # Using BCM numbering, GPIO 17 is Physical Pin 11

# Morse code timing
DOT_DURATION = 0.2  # seconds

# Morse code dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    ' ': '/'
}

def blink_dot():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(DOT_DURATION)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(DOT_DURATION)

def blink_dash():
    GPIO.output(LED_PIN, GPIO.HIGH)
    time.sleep(3 * DOT_DURATION)
    GPIO.output(LED_PIN, GPIO.LOW)
    time.sleep(DOT_DURATION)

def send_morse_code(message, repetitions):
    for _ in range(repetitions):
        for char in message.upper():
            if char in MORSE_CODE_DICT:
                code = MORSE_CODE_DICT[char]
                for symbol in code:
                    if symbol == '.':
                        blink_dot()
                    elif symbol == '-':
                        blink_dash()
                    elif symbol == '/':
                        time.sleep(7 * DOT_DURATION)
                time.sleep(3 * DOT_DURATION)
            else:
                print(f"Unsupported character: {char}")
        time.sleep(7 * DOT_DURATION)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 send.py <repetitions> <message>")
        sys.exit(1)

    repetitions = int(sys.argv[1])
    message = sys.argv[2]

    GPIO.setmode(GPIO.BCM)  # Set the GPIO mode to BCM numbering
    GPIO.setup(LED_PIN, GPIO.OUT)  # Set up the LED pin as an output

    try:
        send_morse_code(message, repetitions)
    finally:
        GPIO.cleanup()  # Clean up the GPIO settings after execution

