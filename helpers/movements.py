#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor, SpeedDPS, SpeedPercent
from helpers.config import MAX_POS, MIN_POS, MOTOR1_DIRECTION, MOTOR2_DIRECTION, MOTOR1_RATIO, MOTOR2_RATIO
import math
from helpers.kinematics import inverse_kinematics

l1_motor = LargeMotor(OUTPUT_A)
l2_motor = LargeMotor(OUTPUT_B)
l1_motor_zero = 0
l2_motor_zero = 0
l1_motor_current = 0
l2_motor_current = 0

def calibrate_zero():
    """Calibrate the zero position of the robot arm."""
    global l1_motor_zero, l2_motor_zero
    l1_motor_zero = l1_motor.degrees
    l2_motor_zero = l2_motor.degrees


def move_to_joint_angles(theta1, theta2):
    # assert l1_motor_zero is not None and l2_motor_zero is not None, "Motors must be calibrated before moving."
    global l1_motor_current, l2_motor_current
    motor1_target = (theta1 - l1_motor_current) * MOTOR1_DIRECTION * MOTOR1_RATIO
    motor2_target = (theta2 - l2_motor_current) * MOTOR2_DIRECTION * MOTOR2_RATIO

    l1_motor.on_for_degrees(SpeedDPS(60), motor1_target, brake=True, block=False)
    l2_motor.on_for_degrees(SpeedDPS(60), motor2_target+motor1_target, brake=True, block=False)
    l1_motor.wait_while("running")
    l2_motor.wait_while('running')

    l1_motor_current = theta1
    l2_motor_current = theta2

def get_joint_angles():
    """Return the current joint angles (theta1, theta2) in degrees."""
    assert l1_motor_zero is not None and l2_motor_zero is not None, "Motors must be calibrated before getting joint angles."
    theta1 = (l1_motor.degrees - l1_motor_zero) / (MOTOR1_DIRECTION * MOTOR1_RATIO)
    theta2 = (l2_motor.degrees - l2_motor_zero) / (MOTOR2_DIRECTION * MOTOR2_RATIO)
    return theta1, theta2


def move_to_position(x, y):
    """
    Move the robot arm to the specified (x, y) position.
    The angles are numerical angles calculated by the inverse kinematics function."""
    (theta1_numerical, theta2_numerical), (theta1_analytical, theta2_analytical) = inverse_kinematics(x, y)
    move_to_joint_angles(theta1_numerical, theta2_numerical)
    return theta1_numerical, theta2_numerical, theta1_analytical, theta2_analytical