PRECISION_VALUES = 2


class Person:

    count = 0

    """
    This class defines a generic person.

    Attributes: first (name), last (name), weight (in lbs), height (in inches)
    """

    def __init__(self, first, last, weight, height):
        self.first_name = first
        self.last_name = last
        self.weight_in_lbs = weight
        self.height_in_inches = height
        Person.count = Person.count + 1

    def calc_bmi(self):

        return (self.weight_in_lbs * 703) / self.height_in_inches ** 2

    @classmethod
    def print_count(cls, ):
        return cls.count

    @classmethod
    def print_class(cls, ):
        print(cls.first_name, cls.last_name, cls.weight_in_lbs, cls.height_in_inches,
              round((cls.weight_in_lbs * 703) / cls.height_in_inches ** 2, PRECISION_VALUES))

    def bmi_category(self):
        if 18.5 <= self.calc_bmi() <= 25:
            return 'normal weight'
        elif 25 < self.calc_bmi() <= 30:
            return 'overweight'
        elif self.calc_bmi() > 30:
            return 'obese'
        else:
            return 'underweight'


p = Person('Tom', 'Thumb', 150, 62)
p2 = Person('Fred', 'Flint', 225, 57)

print(round(p.calc_bmi(), PRECISION_VALUES))
print(round(p2.calc_bmi(), PRECISION_VALUES))
print(Person.count)
print(Person.print_count())
print(p.bmi_category())
print(p2.bmi_category())
print(p.print_class())
print(p2.print_class())
