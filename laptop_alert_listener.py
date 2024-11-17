# laptop_alert_listener.py
# Python script to listen for alerts from the Raspberry Pi Pico and play a sound

import serial
import time
from playsound import playsound  # Install using: pip install playsound

# Replace 'COM3' with the appropriate port for your Raspberry Pi Pico (e.g., COM4, /dev/ttyUSB0)
pico_serial = serial.Serial('COM3', 115200, timeout=1)
time.sleep(2)  # Wait for serial connection to initialize

while True:
  if pico_serial.in_waiting > 0:
    data = pico_serial.readline().decode('utf-8').strip()
    if data == 'ALERT':
      playsound('alert_sound.mp3')  # Play the alert sound file
