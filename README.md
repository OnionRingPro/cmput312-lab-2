# CMPUT 312 Lab 2

## Section 2.3 measurements

Connect the touch sensor to input port 1. Place the robot in the defined zero
configuration, then run one of the following commands on the EV3:

```bash
python3 2.3_measurements.py distance
python3 2.3_measurements.py angle
```

For distance mode, record the two endpoints. For angle mode, record the
intersection first, followed by one point on each line. Each point is captured
after a complete press and release of the touch sensor. The result is printed
in the terminal and displayed on the EV3 screen.