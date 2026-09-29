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


def inverse_kinematics(x, y, l1, l2, error, initial_guess=(0.0, 0.0)):
    """
    Return an analytical inverse-kinematics solution in degrees. 
    Each angle is normalized to the range [-180, 180).
    """
    if l1 <= 0 or l2 <= 0:
        raise ValueError("Link lengths must be positive")
    if error < 0:
        raise ValueError("Error tolerance must be non-negative")

    try:
        guess1, guess2 = initial_guess
        guess1 = float(guess1)
        guess2 = float(guess2)
    except (TypeError, ValueError):
        raise ValueError("initial_guess must contain two angles")

    distance = math.hypot(x, y)
    minimum_reach = abs(l1 - l2)
    maximum_reach = l1 + l2
    if distance > maximum_reach + error or distance < minimum_reach - error:
        raise ValueError("Target position is unreachable")


    ## TODO: Continue here.



def _normalize_angle(angle):
    """Normalize an angle in degrees to the range [-180, 180)."""
    return (angle + 180.0) % 360.0 - 180.0


def _angular_difference(angle1, angle2):
    """Return the smallest signed difference between two degree angles."""
    return _normalize_angle(angle1 - angle2)
