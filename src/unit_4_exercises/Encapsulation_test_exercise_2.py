class Artist:
    """
    This class defines an artist.

    Attributes: name, medium, style, famous_artwork
    """

    def __init__(self, name: str, medium: str, style: str, famous_artwork: str):
        self.__name = name
        self.__medium = medium
        self.__style = style
        self.__famous_artwork = famous_artwork

    def helper_name(self):
        return self.__name

    def helper_medium(self):
        return self.__medium

    def helper_style(self):
        return self.__style

    def helper_famous_artwork(self):
        return self.__famous_artwork


my_artist = Artist('Bill Watterson', 'ink and paper', 'cartoons', 'Calvin and Hobbes')

print(my_artist.helper_name())
print(my_artist.helper_medium())
print(my_artist.helper_style())
print(my_artist.helper_famous_artwork())
