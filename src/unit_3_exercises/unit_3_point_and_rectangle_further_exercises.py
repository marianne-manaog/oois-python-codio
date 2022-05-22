import copy

from unit_3_point_exercises import distance_between_points, Point
from unit_3_rectangle_exercises import Rectangle


class Circle:
    """
    A class defining a circle of a given center and radius.

    Attributes:
        center: Point
            a center point with x and y coordinates.
        radius: float
            the radius of a circle.
    """

    def __init__(self, center: Point, radius: float):
        self.center = center
        self.radius = radius


def point_in_circle(circle: Circle, point: Point) -> bool:
    """
    Check if a point lies in or on the boundary of a circle.

    Args:
        circle: Circle
            a circle object.
        point: Point
            a point object.

    Returns:
                True if a point lies in or on the boundary of a circle, False otherwise.
    """

    if distance_between_points(circle.center, point) <= circle.radius:
        return True
    else:
        return False


def rect_in_circle(circle: Circle, rectangle: Rectangle) -> bool:
    """
    Checks whether a rectangle lies in or on a circle.

    Args:
            circle: Circle
                    a circle object.
            rectangle: Rectangle
                    a rectangle object.
    Returns:
                True if a rectangle lies in or on the boundary of a circle, False otherwise.
    """

    corner_point = copy.copy(rectangle.corner)
    if not point_in_circle(circle, corner_point):
        return False

    corner_point.x += rectangle.width
    if not point_in_circle(circle, corner_point):
        return False

    corner_point.y -= rectangle.height
    if not point_in_circle(circle, corner_point):
        return False

    corner_point.x -= rectangle.width
    if not point_in_circle(circle, corner_point):
        return False

    return True


def rect_circle_overlap(circle, rectangle) -> bool:
    """
    Checks whether any corner points of a rectangle lie in or on a circle.

    Args:
        circle: Circle
                a circle object.
        rectangle: Rectangle
                a rectangle object.
    Returns:
            True if any corner points of a rectangle lie in or on the boundary of a circle, False otherwise.
    """
    corner_point = copy.copy(rectangle.corner)
    if point_in_circle(point=corner_point, circle=circle):
        return True

    corner_point.x += rectangle.width
    if point_in_circle(point=corner_point, circle=circle):
        return True

    corner_point.y -= rectangle.height
    if point_in_circle(point=corner_point, circle=circle):
        return True

    corner_point.x -= rectangle.width
    if point_in_circle(point=corner_point, circle=circle):
        return True

    return False


def main():
    box = Rectangle(width=100., height=200., corner=Point(x=50., y=50.))

    circle = Circle(center=Point(x=150., y=100.), radius=75.)

    print(point_in_circle(circle, box.corner))
    print(rect_in_circle(circle, box))
    print(rect_circle_overlap(circle, box))


if __name__ == '__main__':
    main()
