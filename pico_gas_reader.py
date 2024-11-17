# pico_gas_reader.py
# MicroPython script to read gas sensor data and send an alert signal to the laptop

from machine import ADC, Pin, UART
import utime

adc = ADC(Pin(26))  # Connect the gas sensor's analog output to GP26 on the Pico
uart = UART(0, baudrate=115200)  # Initialize UART for serial communication
threshold = 500  # Gas detection threshold; adjust based on sensor calibration

while True:
  gas_value = adc.read_u16()  # Read analog value from the gas sensor
  if gas_value > threshold:
      uart.write('ALERT\n')  # Send an alert signal to the laptop
  utime.sleep(0.5)  # Wait for 0.5 seconds before the next reading
