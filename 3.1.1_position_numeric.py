#!/usr/bin/env python3
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

from helpers.kinematics import forward_kinematics
from helpers.movements import get_joint_angles, move_to_joint_angles, calibrate_zero, move_to_position
from helpers.write_files import write_to_file

touch_sensor = TouchSensor(INPUT_1)

def move(x,y):
    """Move the robot arm to the specified (x, y) position numerically."""
    theta1, theta2 = move_to_position(x, y, numeric=True)
    (x, y) = forward_kinematics(theta1, theta2)
    return theta1, theta2, (x, y)


def main():
    test_positions = [
        (0.12, 0.14)
    ]

    text = ""
    calibrate_zero()  # Calibrate the zero position before moving
    for x, y in test_positions:
        theta1, theta2, final_pos = move(x, y)
        text += "Moved to position: [x={}, y={}]\n".format(x, y)
        text += "Numerical angles: [theta1={:.2f}, theta2={:.2f}]\n".format(theta1, theta2)
        text += "Final position: x={:.3f}, y={:.3f}\n".format(final_pos[0], final_pos[1])
        text += "================================================================================\n\n\n"
    print(text)
    write_to_file(text, "out/position_results.txt")

if __name__ == '__main__':
    main()

    
