from ev3dev2.motor import OUTPUT_A, OUTPUT_B, LargeMotor, SpeedDPS, SpeedPercent
from helpers.config import MAX_POS, MIN_POS
import math

def move_to_position(x_pos: float, y_pos: float):
    dist = math.sqrt((x_pos * x_pos) + (y_pos * y_pos))
    assert dist <= MAX_POS and dist >= MIN_POS
    