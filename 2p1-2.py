import math


class Rational:
    def __init__(self, numerator=None, denominator=None):
        if numerator is None:
            numerator = 1
        else:
            if not isinstance(numerator, int):
                raise ValueError("Numerator isn't int")
        if denominator is None:
            denominator = 1
        else:
            if not isinstance(denominator, int):
                raise ValueError("Denominator isn't int")
            if denominator == 0:
                raise ValueError("Denominator can't be zero")
        divisor = math.gcd(numerator, denominator)
        self.__num = numerator // divisor
        self.__den = denominator // divisor

    @property
    def show(self):
        return f'{self.__num}/{self.__den}'

    @property
    def show_float(self):
        return self.__num / self.__den


a = Rational()
print(a.show)
print(a.show_float)
