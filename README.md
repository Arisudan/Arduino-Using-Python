# Arduino Blinking LED using Python with pyFirmata

## Overview
This project demonstrates how to control an Arduino board using Python with the `pyFirmata` library. The example showcases the basic blinking LED program, where an LED connected to an Arduino board blinks at a specified interval.

## Prerequisites
Before running this project, ensure you have the following:
- **Arduino Board** (e.g., Arduino Uno, Mega, or compatible board)
- **LED** (if using an external LED) or built-in LED on Pin 13
- **USB Cable** to connect the Arduino to the computer
- **Computer with Python installed**
- **Arduino IDE** to upload the Firmata firmware
- **pyFirmata library** installed in Python

## Installation & Setup
### Step 1: Upload StandardFirmata to Arduino
1. Open the **Arduino IDE**.
2. Go to **File → Examples → Firmata → StandardFirmata**.
3. Select your **board type** and the **correct COM port**.
4. Upload the `StandardFirmata` sketch to the Arduino.

### Step 2: Install pyFirmata
To communicate with Arduino using Python, install the `pyFirmata` library:
```sh
pip install pyfirmata
```

## Running the Blinking LED Code
1. Clone this repository:
   ```sh
   git clone git clone https://github.com/Arisudan/Arduino-Using-Python.git
   cd Arduino-Using-Python
   ```
2. Run the Python script:
   ```sh
   python blink.py
   ```

## Code Explanation
The `blink.py` script contains:
```python
import pyfirmata
import time

board = pyfirmata.Arduino('COM3')  # Change 'COM3' to your Arduino's port
led_pin = board.get_pin('d:13:o')  # Pin 13 as an output

while True:
    led_pin.write(1)  # Turn LED on
    time.sleep(1)      # Wait 1 second
    led_pin.write(0)  # Turn LED off
    time.sleep(1)      # Wait 1 second
```
### Explanation:
- `pyfirmata.Arduino('COM3')`: Connects to the Arduino board on the specified port.
- `board.get_pin('d:13:o')`: Selects **digital pin 13** as an **output**.
- Inside an infinite loop, the LED is turned **on**, waits **1 second**, turned **off**, and repeats.

## Customization
- Change `led_pin = board.get_pin('d:13:o')` to use a different digital pin.
- Modify the `time.sleep(1)` values to change the blink speed.

## Troubleshooting
- If the Arduino is not detected, check the COM port and replace `'COM3'` with the correct port (`/dev/ttyUSB0` on Linux/Mac).
- Ensure `StandardFirmata` is uploaded to the Arduino.
- Verify that `pyfirmata` is correctly installed using `pip list`.

## License
This project is open-source and available under the **MIT License**.

## Contributing
Feel free to fork this repository, create pull requests, or report issues. Contributions are welcome!

---
### Author: [ARISUDAN TH]
GitHub: [https://github.com/Arisudan]

