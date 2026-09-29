#!/usr/bin/env python3
from helpers.movement import get_motor_angles
import time
from ev3dev2.display import Display

lcd = Display()

def main():
    t = 60
    dt = 0.1
    for i in range(int(t / dt)):
        angles = get_motor_angles()
        lcd.text_pixels(
            "L1 angle: " + str(angles[0]) + "\nL2 angle: " + str(angles[1])
        )
        lcd.update()
        
        time.sleep(dt)

if __name__ == "__main__":
    main()