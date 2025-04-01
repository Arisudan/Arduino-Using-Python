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
# **Servo Motor Control with Arduino and Python (pyFirmata)**

## **Overview**
This project demonstrates how to interface and control a **Servo Motor** using an **Arduino** board and Python with the `pyFirmata` library. The script moves the servo motor between **0°, 90°, and 180°** in an infinite loop.

## **Hardware Requirements**
- **Arduino Board** (Uno, Mega, Nano, etc.)
- **Servo Motor** (e.g., SG90, MG995)
- **External Power Supply** (for high-torque servos)
- **Jumper Wires** for connections

## **Software Requirements**
- **Arduino IDE** (for uploading the Firmata sketch)
- **Python 3.x** (with `pyFirmata` installed)
- **pyFirmata Library** (to communicate with Arduino)

## **Step-by-Step Instructions**

### **Step 1: Install Required Libraries**
Before running the Python script, install `pyFirmata` using:
```bash
pip install pyfirmata
```

### **Step 2: Upload Firmata to Arduino**
1. Open **Arduino IDE**.
2. Go to **File** → **Examples** → **Firmata** → **StandardFirmata**.
3. Select the correct **Board** and **Port**.
4. Click **Upload** to flash the Firmata firmware.

### **Step 3: Connect the Servo Motor**
Connect the **Servo Motor** to the Arduino as follows:

| **Servo Motor** | **Arduino** |
|----------------|------------|
| VCC (Red)      | 5V         |
| GND (Black/Brown) | GND    |
| Signal (Yellow/White) | Digital Pin 9 |

### **Step 4: Python Code to Control Servo Motor**
Save the following Python script as `servo_motor.py`:

```python
import pyfirmata
import time

# Define the COM port where Arduino is connected
board = pyfirmata.Arduino('COM5')  # Change COM port as per your system

# Define the servo motor pin
servo = board.get_pin('d:9:s')  # Digital pin 9

time.sleep(2)  # Allow time for Arduino to initialize

try:
    while True:
        print("Moving to 0°")
        servo.write(0)   
        time.sleep(1)

        print("Moving to 90°")
        servo.write(90)  
        time.sleep(1)

        print("Moving to 180°")
        servo.write(180) 
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping servo...")
    board.exit()
```

### **Step 5: Run the Python Script**
After wiring and uploading Firmata, run the script using:
```bash
python servo_motor.py
```

### **Expected Output**
- The **servo motor** moves to **0°**, waits for **1 second**, then moves to **90°**, then **180°**, and repeats.
- The process continues **until manually stopped** using **Ctrl + C**.

## **Troubleshooting**
- **Error: SerialException ("WriteFile failed")**
  - Ensure **no other program** (e.g., Serial Monitor) is using the Arduino's COM port.
  - Try **restarting the computer** and re-uploading the **Firmata** sketch.
- **Servo motor not moving**
  - Check **wiring** and ensure **Firmata** is uploaded correctly.
  - Increase the **delay** (`time.sleep()`) in the script if needed.
  - If using a **high-torque servo**, use an **external power source**.

---

## **Conclusion**
This project provides a simple way to **interface and control a servo motor** with **Arduino using Python** and `pyFirmata`. The **Firmata protocol** allows Python to control hardware without writing custom Arduino sketches.

---
### Author: [ARISUDAN TH]
GitHub: [https://github.com/Arisudan]

