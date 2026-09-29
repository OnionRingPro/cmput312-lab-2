#!/usr/bin/env python3
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor, SpeedDPS, SpeedPercent
from helpers.config import MAX_POS, MIN_POS
import math

l1_motor = LargeMotor(OUTPUT_A)
l2_motor = LargeMotor(OUTPUT_B)

def move_l1_to(angle: float):
    pass

def get_motor_angles() -> tuple:
    """Returns both motor angles

    Returns:
        tuple[float, float]: Returns both motor angles with L1 being at index 0 and L2 being at index 1
    """
    return l1_motor.degrees, l2_motor.degrees