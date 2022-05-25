import random


class Lottery:

    def shuffle(self):
        results = []
        for i in range(5):
            results.append(random.randint(1, 20))
        return results


class Powerball(Lottery):

    def shuffle(self):
        results = []
        for i in range(6):
            results.append(random.randint(1, 99))
        return results
