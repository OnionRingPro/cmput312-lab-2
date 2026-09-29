#!/usr/bin/env python3
"""Measure a distance or an angle by recording robot end-effector points.

Before starting this program, place the arm in the same zero configuration used
for the forward-kinematics model.  Run one of:

    python3 2.3_measurements.py distance
    python3 2.3_measurements.py angle
"""

import argparse

from ev3dev2.display import Display
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import TouchSensor

from helpers.geometry import angle_between, distance_between
from helpers.kinematics import forward_kinematics
from helpers.movements import calibrate_zero, get_joint_angles


lcd = Display()
touch_sensor = TouchSensor(INPUT_1)


def show(message):
    """Show a short message on both the terminal and the EV3 screen."""
    print(message)
    lcd.clear()
    lcd.text_pixels(message, x=0, y=0)
    lcd.update()


def record_point(point_number, description):
    """Wait for one sensor click, then return the current (x, y) position."""
    show("Point {}:\n{}\nPress sensor".format(point_number, description))

    # wait_for_bump waits for a complete press-and-release cycle.  This keeps
    # one long press from being recorded as two different points.
    touch_sensor.wait_for_bump()

    theta1, theta2 = get_joint_angles()
    point = forward_kinematics(theta1, theta2)
    print(
        "Recorded point {}: theta=({:.2f}, {:.2f}) deg, "
        "position=({:.4f}, {:.4f}) m".format(
            point_number, theta1, theta2, point[0], point[1]
        )
    )
    return point


def measure_distance():
    """Record two points and display the Euclidean distance between them."""
    point1 = record_point(1, "First location")
    point2 = record_point(2, "Second location")
    distance_m = distance_between(point1, point2)

    show("Distance:\n{:.4f} m\n{:.2f} cm".format(distance_m, distance_m * 100))
    return point1, point2, distance_m


def measure_angle():
    """Record an intersection and two line points, then display their angle."""
    vertex = record_point(1, "Intersection")
    point1 = record_point(2, "On first line")
    point2 = record_point(3, "On second line")

    try:
        angle_deg = angle_between(vertex, point1, point2)
    except ValueError as error:
        show("Invalid points:\n{}".format(error))
        raise

    show("Smaller angle:\n{:.2f} degrees".format(angle_deg))
    return vertex, point1, point2, angle_deg


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("distance", "angle"))
    args = parser.parse_args()

    # The arm must be physically placed at theta1 = theta2 = 0 before this
    # call.  Encoder readings after calibration are measured from that pose.
    show("Set arm to zero.\nPress sensor")
    touch_sensor.wait_for_bump()
    calibrate_zero()

    if args.mode == "distance":
        measure_distance()
    else:
        measure_angle()


if __name__ == "__main__":
    main()
