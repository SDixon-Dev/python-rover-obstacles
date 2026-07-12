from control import choose_action

# Collision danger threshold used throughout the tests.
# Any sensor reading less than or equal to this value is
# considered too close to an obstacle.
THRESHOLD = 0.1

# Each test consists of:
# (Scenario name, Sensor 1, Sensor 2, Sensor 3, Sensor 4, Expected Result)
#
# Sensor order is:
#   s1 = North
#   s2 = East
#   s3 = South
#   s4 = West
#
# The expected result is the movement direction the rover
# should choose according to the coursework specification.
tests = [
    ("Scenario 1", 0.09, 0.11, 0.11, 0.11, "S"),
    ("Scenario 2", 0.11, 0.09, 0.11, 0.11, "W"),
    ("Scenario 3", 0.11, 0.11, 0.09, 0.11, "N"),
    ("Scenario 4", 0.11, 0.11, 0.11, 0.09, "E"),
    ("Scenario 5", 0.09, 0.09, 0.11, 0.11, "SW"),
    ("Scenario 6", 0.09, 0.11, 0.09, 0.11, "E or W"),
    ("Scenario 7", 0.09, 0.11, 0.11, 0.09, "SE"),
    ("Scenario 8", 0.11, 0.09, 0.09, 0.11, "NW"),
    ("Scenario 9", 0.11, 0.09, 0.11, 0.09, "N or S"),
    ("Scenario 10", 0.11, 0.11, 0.09, 0.09, "NE"),
    ("Scenario 11", 0.09, 0.09, 0.11, 0.09, "S"),
    ("Scenario 12", 0.09, 0.09, 0.09, 0.11, "W"),
    ("Scenario 13", 0.09, 0.11, 0.09, 0.09, "E"),
    ("Scenario 14", 0.11, 0.09, 0.09, 0.09, "N"),
    ("Scenario 15", 0.11, 0.11, 0.11, 0.11, "Continue"),
    ("Scenario 16", 0.09, 0.09, 0.09, 0.09, "Trapped"),
]

print("Running rover obstacle avoidance tests...\n")

passed = 0

# Execute each test in turn.
for name, s1, s2, s3, s4, expected in tests:

    # Call the function being tested.
    result = choose_action(s1, s2, s3, s4, THRESHOLD)

    # Compare the returned value against the expected answer.
    if result == expected:
        print(f"{name}: PASS")
        passed += 1
    else:
        print(f"{name}: FAIL")
        print(f"  Expected: {expected}")
        print(f"  Received: {result}")

# Display an overall summary once every test has finished.
print(f"\nPassed {passed}/{len(tests)} tests.")