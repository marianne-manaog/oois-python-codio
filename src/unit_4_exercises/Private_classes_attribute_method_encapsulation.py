class PrivateClass:

    def __init__(self):
        self.__private_attribute = "I am a private attribute"

    def __private_method(self):
        return "I am a private method"

    def helper_method(self):
        return self.__private_method()


obj = PrivateClass()
print(obj.helper_method())


class TestClass:

    def __init__(self):
        self._attr = 1
        self.attr = 2
        self.__attr = 3

    def helper(self):
        return self.__attr


my_test = TestClass()
print(my_test.helper())
