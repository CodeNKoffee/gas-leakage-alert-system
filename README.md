# Gas Leakage Alert System using DE10-Lite FPGA & Raspberry Pi Pico

## Project Overview

This project aims to create a gas leakage detection system using the DE10-Lite FPGA and Raspberry Pi Pico. The system triggers an alert with a buzzer, lights an LED, and displays a warning message on an LCD display when gas is detected. Custom messages with emojis are shown on the display for added customization.

## Components

- DE10-Lite FPGA (Altera MAX 10M50DAF484C7G)
- Raspberry Pi Pico (Microcontroller)
- MQ-2 or MQ-5 Gas Sensor
- Buzzer Module
- LED (for visual alert)
- LCD Display (16x2 or 20x4)
- Breadboard and connecting wires
- Power supply (5V adapter)
- Enclosure box

## Hardware Setup

1. **Gas Sensor**: Connect the analog output to the Raspberry Pi Pico's ADC pin.
2. **Raspberry Pi Pico to FPGA**: Establish a UART/GPIO connection to transmit gas detection signals.
3. **Alert Outputs**:
   - Buzzer: Connect to an output pin on the FPGA.
   - LED: Connect to another output pin on the FPGA.
   - LCD Display: Connect via GPIO or an I2C/SPI interface.

## Software and Firmware Overview

### MicroPython Code (Raspberry Pi Pico)

- Reads the gas sensor data via an ADC pin.
- Sets a threshold to detect gas levels and signals the FPGA if the threshold is crossed.
- **File**: `pico_gas_reader.py`

### VHDL Code (DE10-Lite FPGA)

- Processes signals from the Raspberry Pi Pico.
- Activates the buzzer, lights the LED, and displays messages on the LCD.
- Customizable to show emojis and various alert messages.
- **File**: `gas_alert_system.vhd`

## File Descriptions

1. **`pico_gas_reader.py`**
   - Script to read data from the gas sensor and transmit it to the FPGA.
   - Includes a threshold check and GPIO control to signal the FPGA.

2. **`gas_alert_system.vhd`**
   - VHDL code to process the input from the Raspberry Pi Pico and control the alert outputs (buzzer, LED, LCD).
   - Includes logic for custom messages with emojis on the LCD display.

3. **`lcd_driver.vhd`**
   - LCD control logic for handling message display with special characters and emojis.

## Implementation Steps

1. **Connect and Configure the Hardware**:
   - Assemble all components as per the wiring diagram provided in this project.
   - Ensure proper connections between the Raspberry Pi Pico and the DE10-Lite FPGA.

2. **Write and Upload MicroPython Code**:
   - Upload `pico_gas_reader.py` to the Raspberry Pi Pico using a tool like Thonny IDE.

3. **Implement and Synthesize VHDL Code**:
   - Use Quartus Prime to write, compile, and synthesize `gas_alert_system.vhd`.
   - Load the bitstream to the DE10-Lite FPGA.

4. **Test and Calibrate**:
   - Test the gas sensor by simulating gas presence and observe the response.
   - Adjust the threshold value as needed in the MicroPython code.

## Assembly Tips

- Use breadboards for prototyping and ensure secure connections for reliable testing.
- Organize the components inside an enclosure to create a professional-looking product.
- Label connections and ports for easy identification during setup and troubleshooting.

## Tutorials and References

1. **MicroPython on Raspberry Pi Pico**:
   - [Official MicroPython Documentation](https://docs.micropython.org/en/latest/rp2/quickref.html)
   - [Tutorial on Using ADC with MicroPython](https://randomnerdtutorials.com/micropython-adc-analog-read-raspberry-pi-pico/)

2. **VHDL Coding and FPGA Programming**:
   - [Intel Quartus Prime Introduction](https://www.intel.com/content/www/us/en/docs/programmable/683472/current/using-quartus-prime-software.html)
   - [LCD Interface with FPGA](https://www.fpga4student.com/2017/05/lcd-interfacing-with-fpga.html)

3. **LCD Display with FPGA**:
   - [VHDL Code for LCD](https://www.electronicwings.com/vhdl/lcd-16x2-interfacing-with-fpga)

## Future Improvements

- Add audio output to read alert messages aloud using a speech synthesis module.
- Implement additional sensors (e.g., temperature) for extended functionality.
