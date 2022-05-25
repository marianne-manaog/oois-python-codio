class Characters:
    """
    This class defines characters.

    Attributes: phrases
    """

    def __init__(self, phrases):
        self.phrases = phrases

    def __lt__(self, other):
        sum_self = sum(len(ph) for ph in self.phrases)
        sum_other = sum(len(phr) for phr in other.phrases)
        return sum_self < sum_other

    def __gt__(self, other):
        sum_self = sum(len(ph) for ph in self.phrases)
        sum_other = sum(len(phr) for phr in other.phrases)
        return sum_self > sum_other

    def __eq__(self, other):
        sum_self = sum(len(ph) for ph in self.phrases)
        sum_other = sum(len(phr) for phr in other.phrases)
        return sum_self == sum_other


sample_phrases1 = ['cat in the hat', 'green eggs and ham', 'the lorax']
sample_phrases2 = ['the taming of the shrew', 'hamlet', 'othello']

c1 = Characters(sample_phrases1)
c2 = Characters(sample_phrases2)
print(c1 > c2)  # prints 'True'
print(c1 < c2)  # prints 'False'
print(c1 == c1)  # prints 'True'
