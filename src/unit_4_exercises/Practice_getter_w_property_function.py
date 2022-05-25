class Person:
    """
    This class defines a person.

    Attributes: name, age
    """

    def __init__(self, name, age):
        self._name = name
        self._age = age

    def get_name(self):
        return self._name

    name = property(get_name)

    def get_age(self):
        return self._age

    age = property(get_age)


c = Person("Calvin", 6)
print(c.name)
print(c.age)
