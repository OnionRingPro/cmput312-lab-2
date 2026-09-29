#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor, SpeedDPS, SpeedPercent
from helpers.config import MAX_POS, MIN_POS, MOTOR1_DIRECTION, MOTOR2_DIRECTION, MOTOR1_RATIO, MOTOR2_RATIO
import math

l1_motor = LargeMotor(OUTPUT_A)
l2_motor = LargeMotor(OUTPUT_B)
l1_motor_zero = None
l2_motor_zero = None

def calibrate_zero():
    """Calibrate the zero position of the robot arm."""
    global l1_motor_zero, l2_motor_zero
    l1_motor_zero = l1_motor.degrees
    l2_motor_zero = l2_motor.degrees


def move_to_joint_angles(theta1, theta2):
    assert l1_motor_zero is not None and l2_motor_zero is not None, "Motors must be calibrated before moving."
    motor1_target = (theta1) * MOTOR1_DIRECTION * MOTOR1_RATIO + l1_motor_zero
    motor2_target = (theta2) * MOTOR2_DIRECTION * MOTOR2_RATIO + l2_motor_zero

    l1_motor.on_to_position(SpeedDPS(20), motor1_target, brake=True, block=False)
    l2_motor.on_to_position(SpeedDPS(20), motor2_target, brake=True, block=True)
    l1_motor.wait_while('running')

def get_joint_angles():
    """Return the current joint angles (theta1, theta2) in degrees."""
    assert l1_motor_zero is not None and l2_motor_zero is not None, "Motors must be calibrated before getting joint angles."
    theta1 = (l1_motor.degrees - l1_motor_zero) / (MOTOR1_DIRECTION * MOTOR1_RATIO)
    theta2 = (l2_motor.degrees - l2_motor_zero) / (MOTOR2_DIRECTION * MOTOR2_RATIO)
    return theta1, theta2
