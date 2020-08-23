
class Arithmetic(object):

    def __init__(self, num_a, num_b):
        self.__num_a = num_a
        self.__num_b = num_b

    def add(self):
        return self.__num_a + self.__num_b

    def minus(self):
        return self.__num_a - self.__num_b

    def multiple(self):
        return self.__num_a * self.__num_b
