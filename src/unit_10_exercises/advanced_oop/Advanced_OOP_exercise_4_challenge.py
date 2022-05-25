class Book:
    """
    This class defines a book.

    Attributes: title, author, genre
    """

    def __init__(self, title: str, author: str, genre: str):
        self.title = title
        self.author = author
        self.genre = genre

    def __str__(self):
        return f"The book entitled '{self.title}' and authored by '{self.author}' has a genre '{self.genre}'."

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.genre})"
