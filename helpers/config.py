"""
Store every configs like L1, L2
"""

# This is a mock value, real values are waited to be maesured
L1 = 0.109
L2 = 0.113

MAX_POS = L1 + L2
MIN_POS = abs(L1 - L2)
# ERROR = 0.1 # the small error possible in the measurement