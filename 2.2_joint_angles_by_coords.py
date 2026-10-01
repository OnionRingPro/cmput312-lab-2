#!/usr/bin/env python3
from helpers.kinematics import forward_kinematics
from helpers.movements import get_joint_angles, move_to_joint_angles, calibrate_zero
from helpers.write_files import write_to_file

def move(theta1, theta2):
    """Move the robot arm to the specified joint angles (in degrees)."""
    move_to_joint_angles(theta1, theta2)
    theta1_encoder, theta2_encoder = get_joint_angles()  # Get the actual joint angles after moving
    encoder_pos = forward_kinematics(theta1_encoder, theta2_encoder)
    ideal_pos = forward_kinematics(theta1, theta2)

    return theta1_encoder, theta2_encoder, encoder_pos, ideal_pos

def main():
    test_configurations = [
        (90, 90),  
        (0, -45),
        (-90, 45)
    ]

    calibrate_zero()  # Calibrate the zero position before moving

    text = ""

    for theta1, theta2 in test_configurations:
        theta1_encoder, theta2_encoder, encoder_pos, ideal_pos = move(theta1, theta2)
        text += "theta encoder: [{:.2f}, {:.2f}]\n".format(theta1_encoder, theta2_encoder)
        text += "position encoder: (x,y) = ({:.2f}, {:.2f})\n".format(encoder_pos[0], encoder_pos[1])
        text += "position ideal: (x, y) = ({:.2f}, {:.2f})\n".format(ideal_pos[0], ideal_pos[1])
        text += "=================================================\n"
    print(text)
    write_to_file(text, filename='2.2_log.txt')

if __name__ == '__main__':
    main()
