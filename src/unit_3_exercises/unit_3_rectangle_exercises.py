# This Python file defines the class 'Rectangle' and performs related operations.

import copy

from unit_3_point_exercises import print_point, Point


class Rectangle:
    """
    Represents a rectangle.

    attributes: width (float), height (float), corner (Point).
    """

    def __init__(self, width: float, height: float, corner: Point):
        self.width = width
        self.height = height
        self.corner = corner


box = Rectangle(width=100., height=200., corner=Point(x=0., y=0.))


def find_center(rectangle_obj: Rectangle) -> Point:
    """
    Find the center of a rectangle.

    Args:
        rectangle_obj: Rectangle
                    a rectangle object.

    Returns:
        a center point, along with its cartesian coordinates (x and y).
    """
    center_point_x = rectangle_obj.corner.x + rectangle_obj.width/2
    center_point_y = rectangle_obj.corner.y + rectangle_obj.height/2
    center_point = Point(x=center_point_x, y=center_point_y)
    return center_point


center_pt = find_center(box)
print("The coordinates of the center of the rectangle 'box' are: ")
print_point(center_pt)


def grow_rectangle(rectangle_obj: Rectangle, delta_width: float, delta_height: float) -> None:
    """
    Add a number to the width and the height of a rectangle.

    Args:
        rectangle_obj: Rectangle
                    a rectangle object.
        delta_width: float
                    a number to be added to the width.
        delta_height: float
                    a number to be added to the height.
    """
    rectangle_obj.width += delta_width
    rectangle_obj.height += delta_height


grow_rectangle(rectangle_obj=box, delta_width=50, delta_height=100)

updated_center_pt = find_center(box)
print("The coordinates of the center of the updated rectangle 'box' are: ")
print_point(updated_center_pt)


def move_rectangle(rectangle_obj: Rectangle, dx: float, dy: float) -> None:
    """
    Move rectangle by adding number dx and another number dy to the
    coordinates of the corner.

    Args:
        rectangle_obj: Rectangle
                    a rectangle object.
        dx: float
            a number to be added to the x coordinate of the corner.
        dy: float
            a number to be added to the y coordinate of the corner.
    """
    rectangle_obj.corner.x += dx
    rectangle_obj.corner.y += dy


print('Initial corner of the rectangle is: ')
print_point(box.corner)

move_rectangle(rectangle_obj=box, dx=2., dy=3.)

print('Updated corner of the rectangle is: ')
print_point(box.corner)


def move_rectangle_w_copy(rectangle_obj: Rectangle, dx: float, dy: float) -> Rectangle:
    """
    Create new rectangle and move it by adding number dx and another number dy to the
    coordinates of its corner.

    Args:
        rectangle_obj: Rectangle
                    the original rectangle object.
        dx: float
            a number to be added to the x coordinate of the corner of the new rectangle
            (a copy of the original rectangle).
        dy: float
            a number to be added to the y coordinate of the corner of the new rectangle
            (a copy of the original rectangle).

    Returns:
        a copy of the original rectangle with updated coordinates based on the input dx and dy.
    """
    new_rectangle_moved = copy.deepcopy(rectangle_obj)
    new_rectangle_moved.corner.x += dx
    new_rectangle_moved.corner.y += dy

    return new_rectangle_moved


print('Corner of the original rectangle is: ')
print_point(box.corner)

new_rectangle = move_rectangle_w_copy(rectangle_obj=box, dx=6., dy=10.)

print('Corner of the copy/moved rectangle is: ')
print_point(new_rectangle.corner)

print('Corner of the original rectangle is: ')
print_point(box.corner)
