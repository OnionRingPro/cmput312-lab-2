"""Kinematics helpers for the robot arm."""

import math

def forward_kinematics(theta1, theta2, l1, l2):
    """Return the end-effector position (x, y).
    """
    if l1 < 0 or l2 < 0:
        raise ValueError("Link lengths must be non-negative")

    theta1_radians = math.radians(theta1)
    theta12_radians = math.radians(theta1 + theta2)

    x = l1 * math.cos(theta1_radians) + l2 * math.cos(theta12_radians)
    y = l1 * math.sin(theta1_radians) + l2 * math.sin(theta12_radians)

    return x, y


def inverse_kinematics(x, y, l1, l2):
    """
    Return an anlytical solution
    input: x, y, l1, l2
    return: (theta1, theta2) in degrees
    """
    if l1 < 0 or l2 < 0:
        raise ValueError("Link lengths must be non-negative")

    distance = math.hypot(x, y)
    if distance > (l1 + l2):
        raise ValueError("Target position is unreachable")
    # TODO: Need to be implemented.


