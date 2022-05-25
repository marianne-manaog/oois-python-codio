from typing import List


class Band:
    """
    This class defines a musical band.

    Attributes: name, genre, members
    """
    def __init__(self, name: str, genre: str, members: List[str]):
        self.name = name
        self.genre = genre
        self.members = members

    def __str__(self):
        return f"{self.name} is a {self.genre} band."

    def __repr__(self):
        return f"Band({self.name}, {self.genre}, {self.members})"


dead = Band('The Grateful Dead', 'rock\'n roll', ['Jerry', 'Bob', 'Mickey', 'Bill', 'Phil', 'Pigpen'])

print(dead)

print(repr(dead))
