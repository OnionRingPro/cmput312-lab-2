"""
Store every configs like L1, L2
"""

L1 = 0.109
L2 = 0.113

MAX_POS = L1 + L2
MIN_POS = abs(L1 - L2)
ERROR = 0.001 # the small error possible in the measurement
MAX_INTERATION = 1000
INITIAL_GUESS = (10, 30) # initial guess for IK newton method, (10deg, 30deg)

# Motor ratios
MOTOR1_RATIO = 1.0
MOTOR2_RATIO = 5 / 3

# If the motor moves positive, the angle increases, then the direction parameter is 1.
MOTOR1_DIRECTION = 1
MOTOR2_DIRECTION = 1

FILE_NAME = "log.txt"