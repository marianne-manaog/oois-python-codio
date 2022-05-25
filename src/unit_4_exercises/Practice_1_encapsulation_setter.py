class Person:
    """
    This class defines a person.

    Attribute: name
    """

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


c = Person("Calvin")
print(c.name)
c.name = "Hobbes"
print(c.name)
