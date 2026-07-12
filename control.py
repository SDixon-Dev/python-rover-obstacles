def choose_action(s1, s2, s3, s4, t):
    """
    Choose an action for the rover based on its four sensor readings.

    s1: North sensor reading
    s2: East sensor reading
    s3: South sensor reading
    s4: West sensor reading
    t: Collision danger threshold
    """

    # Record whether each direction is blocked.
    north_blocked = s1 <= t
    east_blocked = s2 <= t
    south_blocked = s3 <= t
    west_blocked = s4 <= t

    # All four directions are blocked.
    if north_blocked and east_blocked and south_blocked and west_blocked:
        return "Trapped"

    # Three directions are blocked.
    elif north_blocked and east_blocked and south_blocked and not west_blocked:
        return "W"

    elif north_blocked and east_blocked and not south_blocked and west_blocked:
        return "S"

    elif north_blocked and not east_blocked and south_blocked and west_blocked:
        return "E"

    elif not north_blocked and east_blocked and south_blocked and west_blocked:
        return "N"

    # Two directions are blocked.
    elif north_blocked and east_blocked and not south_blocked and not west_blocked:
        return "SW"

    elif north_blocked and not east_blocked and south_blocked and not west_blocked:
        return "E or W"

    elif north_blocked and not east_blocked and not south_blocked and west_blocked:
        return "SE"

    elif not north_blocked and east_blocked and south_blocked and not west_blocked:
        return "NW"

    elif not north_blocked and east_blocked and not south_blocked and west_blocked:
        return "N or S"

    elif not north_blocked and not east_blocked and south_blocked and west_blocked:
        return "NE"

    # One direction is blocked.
    elif north_blocked and not east_blocked and not south_blocked and not west_blocked:
        return "S"

    elif not north_blocked and east_blocked and not south_blocked and not west_blocked:
        return "W"

    elif not north_blocked and not east_blocked and south_blocked and not west_blocked:
        return "N"

    elif not north_blocked and not east_blocked and not south_blocked and west_blocked:
        return "E"

    # No directions are blocked.
    else:
        return "Continue"