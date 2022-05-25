class Airplane:
    """
    This class defines an airplane.

    Attributes: first_class (passengers), business_class (passengers), coach (passengers)
    """

    def __init__(self, first_class, business_class, coach):
        self.first_class = first_class
        self.business_class = business_class
        self.coach = coach

    def total(self):
        return self.first_class + self.business_class + self.coach


class Train:
    """
    This class defines a train.

    Attributes: car1 (passengers), car2 (passengers), car3 (passengers), car4 (passengers), car5 (passengers)
    """

    def __init__(self, car1, car2, car3, car4, car5):
        self.car1 = car1
        self.car2 = car2
        self.car3 = car3
        self.car4 = car4
        self.car5 = car5

    def total(self):
        return self.car1 + self.car2 + self.car3 + self.car4 + self.car5


def passengers(obj):
    print(f'There are {obj.total()} passengers on board.')
