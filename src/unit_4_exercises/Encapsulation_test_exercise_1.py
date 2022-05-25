class Country:
    """
    This class defines a country.

    Attributes: name, capital, population, continent
    """

    def __init__(self, name: str, capital: str, population: int, continent: str):
        self._name = name
        self._capital = capital
        self._population = population
        self._continent = continent


my_country = Country('France', 'Paris', 67081000, 'Europe')

print(my_country._name)
print(my_country._capital)
print(my_country._population)
print(my_country._continent)
