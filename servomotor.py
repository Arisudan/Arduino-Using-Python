import pyfirmata
import time

board = pyfirmata.Arduino('COM5')  
servo = board.get_pin('d:9:s')  

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
