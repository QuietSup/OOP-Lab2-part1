import math


class Rational:
    def __init__(self, numerator=1, denominator=1):
        assert isinstance(numerator, int)
        assert isinstance(denominator, int)
        assert denominator != 0
        divisor = math.gcd(numerator, denominator)
        self.__num = numerator // divisor
        self.__den = denominator // divisor

    def show(self):
        return (str(self.__num), '/', str(self.__div))

    def show_float(self):
        return self.__num / self.__div


a = Rational(2, 4)
print(a.show())
print(a.show_float())
