# Rover Obstacle Avoidance System

A Python solution developed as part of a robotics programming challenge.

## Overview

This project simulates the decision-making logic for a planetary exploration rover equipped with four laser range finders.

The rover determines the safest movement direction based on nearby obstacles detected to its:

- North
- East
- South
- West

If an obstacle is detected within the collision threshold, the rover selects the safest direction to travel.

## Features

- Uses four simulated distance sensors
- Supports all 16 required obstacle scenarios
- Returns movement directions including:

```
N
S
E
W
NE
NW
SE
SW
E or W
N or S
Continue
Trapped
```

- Written entirely using Python `if`, `elif` and `else` statements.

## Files

| File | Description |
|------|-------------|
| control.py | Main rover decision logic |
| test_control.py | Personal testing program |

## Example

```python
from control import choose_action

result = choose_action(
    s1=0.09,
    s2=0.11,
    s3=0.11,
    s4=0.11,
    t=0.1
)

print(result)

# Output:
S
```

## Skills Demonstrated

- Python
- Conditional logic
- Function design
- Software testing
- Problem solving

## Author

Sean Dixon
