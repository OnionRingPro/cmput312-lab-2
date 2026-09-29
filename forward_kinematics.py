from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor
import math

"""
Part 2.1 Basic Robot 
"""
def move_to_position(x_pos: float, y_pos: float):
    assert 