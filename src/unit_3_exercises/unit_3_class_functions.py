class Time:
    """
    Represents the time of the day.

    attributes: hour, minute, second
    """
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second


def print_time(time_obj: Time) -> None:
    """
    Prints a time in string format.

    Args:
        time_obj: Time
                a time object.
    """
    print('%.2d:%.2d:%.2d' % (time_obj.hour, time_obj.minute, time_obj.second))


def is_after(time_obj_first: Time, time_obj_second: Time) -> bool:
    """
    Returns true if the first time were after the second one (false otherwise).

    Args:
        time_obj_first: Time
                        the first time object.
        time_obj_second: Time
                        the second time object.

    Returns:
        True if time_obj_first were after time_obj_second; False otherwise.
    """
    bool_return = (time_obj_first.hour, time_obj_first.minute, time_obj_first.second) > (time_obj_second.hour,
                                                                                         time_obj_second.minute,
                                                                                         time_obj_second.second)
    return bool_return


def check_valid_time(time_obj: Time) -> bool:
    """
    Checks if a time object met set conditions.

    Args:
        time_obj: Time
                a time object.

    Returns:
            True if it were a valid time based on set conditions, False otherwise.
    """
    if time_obj.hour < 0 or time_obj.minute < 0 or time_obj.second < 0:
        return False
    if time_obj.minute >= 60 or time_obj.second >= 60:
        return False
    return True


def convert_int_to_time(seconds: int) -> Time:
    """
    Creates and returns a Time object given input seconds.

    Args:
        seconds: int
                seconds since midnight.

    Returns:
            a Time object given input seconds.
    """
    time_obj = Time()
    minutes, time_obj.second = divmod(seconds, 60)
    time_obj.hour, time_obj.minute = divmod(minutes, 60)
    return time_obj


def convert_time_to_int(time_obj: Time) -> int:
    """
    Computes the number of seconds since midnight.

    Args:
        time_obj: Time
                a time object.

    Returns:
        seconds (int) since midnight.
    """
    minutes = time_obj.hour * 60 + time_obj.minute
    seconds = minutes * 60 + time_obj.second
    return seconds


def increment_time(time_obj: Time, seconds: int) -> Time:
    """
    Adds seconds to a Time object.

    Args:
        time_obj: Time
                a time object.
        seconds: int
                seconds since midnight.

    Return:
        a Time object from seconds (int).
    """
    assert check_valid_time(time_obj)
    seconds += convert_time_to_int(time_obj)
    return convert_int_to_time(seconds)


def add_times(time_obj_first: Time, time_obj_second: Time) -> Time:
    """
    Adds two time objects.

    Args:
        time_obj_first: Time
                        the first Time object.
        time_obj_second: Time
                        the second Time object.

    Returns:
            the sum of the two input Time objects.
    """
    assert check_valid_time(time_obj_first) and check_valid_time(time_obj_second)
    seconds = convert_time_to_int(time_obj_first) + convert_time_to_int(time_obj_second)
    return convert_int_to_time(seconds)
