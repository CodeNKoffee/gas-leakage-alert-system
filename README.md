# Gas Leakage Alert System Using Raspberry Pi Pico and Laptop

## Project Overview

This project is designed to detect gas leakage using a Raspberry Pi Pico and a gas sensor. When gas levels exceed a certain threshold, the system sends a signal to a connected laptop, which plays an alert sound and displays a warning on the LCD (optional).

## Components Required

- Raspberry Pi Pico
- MQ-2 or MQ-5 gas sensor module
- Laptop (for running the alert script)
- Breadboard and jumper wires
- USB cable for connecting the Pico to the laptop
- LCD (optional, if displaying messages is needed)

## Hardware Setup

1. **Gas Sensor Wiring**:

   - Connect the analog output pin of the gas sensor to the `GP26` pin on the Raspberry Pi Pico.
   - Connect `VCC` of the gas sensor to `3.3V` or `5V` on the Pico.
   - Connect `GND` of the sensor to the ground pin on the Pico.

2. **Connect the Raspberry Pi Pico to the Laptop**:
   - Use a micro USB cable to connect the Pico to the laptop for both power and data transfer.

## Software Installation and Setup

1. **MicroPython Setup**:

   - Install MicroPython on the Raspberry Pi Pico using the [official MicroPython installation guide](https://micropython.org/download/rp2-pico/).

2. **Upload MicroPython Code**:

   - Open Thonny IDE.
   - Copy the content of `pico_gas_reader.py` into Thonny.
   - Save and upload the code to the Pico.

3. **Install Python Packages on Laptop**:
   - Ensure Python is installed on your laptop.
   - Install the `playsound` package by running:

     ```bash
     pip install playsound
     ```

## Running the System

1. **Run the MicroPython Script**:

   - Ensure the Raspberry Pi Pico is connected to the laptop.
   - The Pico will start reading gas levels and sending signals if gas is detected.

2. **Run the Laptop Script**:

   - Run `laptop_alert_listener.py` on your laptop:

     ```bash
     python laptop_alert_listener.py
     ```

   - Ensure `alert_sound.mp3` is in the same directory or provide the correct path.

## Usage Notes

- Test and calibrate the threshold value to ensure proper gas detection.
- Replace the COM port in the laptop script with the appropriate port detected by your system.

## Future Enhancements

- Add more sensors (e.g., temperature) for extended safety monitoring.
- Implement a more sophisticated sound alert or integrate with smart home systems for automatic safety measures.
