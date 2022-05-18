# This Python file defines the class 'Point' and uses it to instantiate point objects
# and calculate the distance between them.

import math


class Point:
    """
    Represents a point in 2D space.

    attributes: x (float), y (float), which represent the two cartesian coordinates of a point.
    """

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

# Instantiate object 'point_first' from the 'Point' class
point_first = Point(x=3., y=4.)


def print_point(point_obj: Point) -> None:
    """
    Print x and y coordinates of point object 'p'

    Args:
        point_obj: Point
                a point object
    """
    print('(%g, %g)' % (point_obj.x, point_obj.y))


print_point(point_obj=point_first)

distance = math.sqrt(point_first.x**2 + point_first.y**2)

print('The distance is: ', distance)


def distance_between_points(first_point: Point, second_point: Point) -> float:
    """
    Compute distance between two points

    Args:
        first_point: Point
                    the first point considered
        second_point: Point
                    the second point considered

    Returns:
        the distance (float) between first_point and second_point.
    """

    dist_x = first_point.x - second_point.x
    dist_y = first_point.y - second_point.y
    dist_bw_points = math.sqrt(dist_x**2 + dist_y**2)
    return dist_bw_points


# Instantiate object 'point_second' from the 'Point' class
point_second = Point(x=5., y=7.)

PRECISION_VALS = 3
dist_bw_p1_and_p2 = round(distance_between_points(first_point=point_first, second_point=point_second), PRECISION_VALS)

print('The distance between first and second points is: ', dist_bw_p1_and_p2)
