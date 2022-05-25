import statistics


class Median:
    """
    This class has a method to compute the median on any number (2 or more) of inputs.
    """

    def calculate_median(self, *params):
        median_computed = statistics.median([*params])
        return median_computed


median_obj = Median()
print(median_obj.calculate_median(3, 5, 1, 4, 2))
print(median_obj.calculate_median(8, 6, 4, 2))
print(median_obj.calculate_median(9, 3, 7))
print(median_obj.calculate_median(5, 2))
