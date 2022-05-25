class Cyclist:
    """
    This class defines a cyclist.

    Attributes: name, nationality, nickname
    """

    def __init__(self, name, nationality, nickname):
        self._name = name
        self._nationality = nationality
        self._nickname = nickname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if type(new_name) != str:
            raise TypeError("Names must be expressed as a string")
        self._name = new_name

    @property
    def nationality(self):
        return self._nationality

    @nationality.setter
    def nationality(self, new_nationality):
        if type(new_nationality) != str:
            raise TypeError("Nationalities must be expressed as a string")
        self._nationality = new_nationality

    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self, new_nickname):
        if type(new_nickname) != str:
            raise TypeError("Nicknames must be expressed as a string")
        self._nickname = new_nickname


my_cyclist = Cyclist("Greg LeMond", "American", "Le Montstre")

print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)

my_cyclist.name = "Eddy Merckx"
my_cyclist.nationality = "Belgian"
my_cyclist.nickname = "The Cannibal"

print(my_cyclist.name)
print(my_cyclist.nationality)
print(my_cyclist.nickname)
