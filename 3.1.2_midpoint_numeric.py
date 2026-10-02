#!/usr/bin/env python3
from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

from helpers.kinematics import forward_kinematics
from helpers.movements import get_joint_angles, get_computed_angles, set_position, move_to_joint_angles, calibrate_zero, move_to_position
from helpers.write_files import write_to_file

lcd = Display()
touch_sensor = TouchSensor(INPUT_1)

def move(x,y):
    """Move the robot arm to the specified (x, y) position numerically."""
    theta1, theta2 = move_to_position(x, y, numeric=True)
    (x, y) = forward_kinematics(theta1, theta2)
    return theta1, theta2, (x, y)

def show(message):
    """Show a short message on both the terminal and the EV3 screen."""
    print(message)
    lcd.clear()
    lcd.text_pixels(message, x=0, y=0)
    lcd.update()


def record_point(point_number):
    """Wait for one sensor click, then return the current (x, y) position."""
    show("Point {}, Press sensor".format(point_number))

    # wait_for_bump waits for a complete press-and-release cycle.  This keeps
    # one long press from being recorded as two different points.
    touch_sensor.wait_for_bump()

    theta1, theta2 = get_joint_angles()
    point = forward_kinematics(theta1, theta2)
    return point

def get_midpoint(point1, point2):
    """Calculate the midpoint between two points."""
    x_mid = (point1[0] + point2[0]) / 2
    y_mid = (point1[1] + point2[1]) / 2
    return x_mid, y_mid

def main():
    text = ""
    calibrate_zero()  # Calibrate the zero position before moving

    point1 = record_point(1)
    text += "Recorded point 1: x={:.3f}, y={:.3f}\n".format(point1[0], point1[1])
    point2 = record_point(2)
    text += "Recorded point 2: x={:.3f}, y={:.3f}\n".format(point2[0], point2[1])

    set_position()

    x, y = get_midpoint(point1, point2)
    theta1, theta2, final_pos = move(x, y)
    theta1_read, theta2_read = get_joint_angles()
    theta1_calc, theta2_calc = get_computed_angles()
    text += "Moved to position: [x={}, y={}]\n".format(x, y)
    text += "Numerical angles: [theta1={:.2f}, theta2={:.2f}]\n".format(theta1, theta2)
    text += "Final position: x={:.3f}, y={:.3f}\n".format(final_pos[0], final_pos[1])
    text += "Actual angles: [theta1={:.2f}, theta2={:.2f}]\n".format(theta1_read, theta2_read)
    text += "Computed angles: [theta1={:.2f}, theta2={:.2f}]\n".format(theta1_calc, theta2_calc)
    text += "================================================================================\n\n\n"
    print(text)
    write_to_file(text, "out/position_results.txt")

if __name__ == '__main__':
    main()

    
