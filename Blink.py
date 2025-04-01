import pyfirmata
import time

board = pyfirmata.Arduino('COM3')

led_pin = board.get_pin('d:13:o')

while True:
    led_pin.write(1)  
    time.sleep(1)     
    led_pin.write(0)  
    time.sleep(1)   
