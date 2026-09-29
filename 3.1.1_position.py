#!/usr/bin/env python3
from helpers.kinematics import forward_kinematics, inverse_kinematics
from helpers.movements import get_joint_angles, move_to_joint_angles, calibrate_zero
from helpers.write_files import write_to_file

"""
Receive an input (x,y) and moves the robot end-effector to that position
"""

def move(x,y):
    """Move the robot arm to the specified (x, y) position."""
    calibrate_zero()  # Calibrate the zero position before moving

    (theta1_numerical, theta2_numerical), (theta1_analytical, theta2_analytical) = inverse_kinematics(x, y, initial_guess=(0.0, 0.0))

    move_to_joint_angles(theta1_numerical, theta2_numerical)
    (x, y) = forward_kinematics(theta1_numerical, theta2_numerical)
    return theta1_numerical, theta2_numerical, theta1_analytical, theta2_analytical, (x, y)

def main():
    test_positions = [
        (0.12, 0.14)
    ]

    text = ""

    for x, y in test_positions:
        theta1_numerical, theta2_numerical, theta1_analytical, theta2_analytical, final_pos = move(x, y)
        text += f"Moved to position: [x={x}, y={y}]\n"
        text += f"Numerical angles: [theta1={theta1_numerical:.2f}, theta2={theta2_numerical:.2f}]\n"
        text += f"Analytical angles: [theta1={theta1_analytical:.2f}, theta2={theta2_analytical:.2f}]\n"
        text += f"Final position: x={final_pos[0]:.3f}, y={final_pos[1]:.3f}\n"
        text += "================================================================================\n"

    write_to_file(text)

if __name__ == '__main__':
    main()

    