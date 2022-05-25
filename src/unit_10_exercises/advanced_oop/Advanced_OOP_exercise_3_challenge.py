class Dog:
    """
    This class defines a dog

    Attributes: name, breed
    """

    def __init__(self, name: str, breed: str):
        self.name = name
        self.breed = breed

    def __str__(self):
        return f"The dog is named {self.name} and its breed is {self.breed}."

    def __repr__(self):
        return f"Dog({self.name}, {self.breed})"


dog_1 = Dog('Marceline', 'German Shepherd')
dog_2 = Dog('Cajun', 'Belgian Malinois')
dog_3 = Dog('Daisy', 'Border Collie')
dog_4 = Dog('Rocky', 'Golden Retriever')
dog_5 = Dog('Bella', 'Irish Setter')

list_of_dogs = [dog_1, dog_2, dog_3, dog_4, dog_5]

print(list_of_dogs)
