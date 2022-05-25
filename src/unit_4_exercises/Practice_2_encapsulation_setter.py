class Person:
    """
    This class defines a person.

    Attributes: name, age
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age <= 0:
            raise TypeError("Age must be expressed as a positive number")
        self._age = new_age


c = Person("Calvin", "6")
print(c.name)
print(c.age)
c.age = -17
c.name = "False"
print(c.name)
print(c.age)
