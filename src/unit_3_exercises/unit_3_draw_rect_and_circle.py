import polygon
import turtle

from unit_3_point_exercises import Point
from unit_3_rectangle_exercises import Rectangle
from unit_3_point_and_rectangle_further_exercises import Circle


def draw_circle(turt, circle: Circle) -> None:
    """
    Draws a circle.

    Args:
        turt: Turtle
            a turtle object.
        circle: Circle
            a circle object.
    """
    turt.pu()
    turt.goto(circle.center.x, circle.center.y)
    turt.fd(circle.radius)
    turt.lt(90)
    turt.pd()
    polygon.circle(turt, circle.radius)


def draw_rect(turt, rectangle):
    """
    Draws a rectangle.

    Args:
        turt: Turtle
            a turtle object.
        rectangle: Rectangle
            a rectangle object.
    """
    turt.pu()
    turt.goto(rectangle.corner.x, rectangle.corner.y)
    turt.setheading(0)
    turt.pd()

    for length in rectangle.width, rectangle.height, rectangle.width, rectangle.height:
        turt.fd(length)
        turt.rt(90)


if __name__ == '__main__':
    turtle_object = turtle.Turtle()

    # Draw axes
    length = 400
    turtle_object.fd(length)
    turtle_object.bk(length)
    turtle_object.lt(90)
    turtle_object.fd(length)
    turtle_object.bk(length)

    # Draw rectangle
    box = Rectangle(width=100., height=200., corner=Point(x=50., y=50.))

    draw_rect(turtle_object, box)

    # Draw circle
    circle = Circle(center=Point(x=150., y=100.), radius=75.)

    draw_circle(turtle_object, circle)

    # Wait for user to close window
    turtle.mainloop()

