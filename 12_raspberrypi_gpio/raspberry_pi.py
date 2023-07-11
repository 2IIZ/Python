import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

LED_PIN = 19
BUTTON_PIN = 13

GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
    button_state = GPIO.input(BUTTON_PIN)
    print(button_state)
    time.sleep(0.02)
    if button_state == 1:
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        GPIO.output(LED_PIN, GPIO.LOW)


GPIO.cleanup()