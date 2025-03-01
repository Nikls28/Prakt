from math import gcd
from functools import cmp_to_key

class BigFraction:
    def __init__(self, numerator, denominator):
        """Инициализация дроби с длинными числами."""
        if isinstance(numerator, list):
            self.numerator = int(''.join(map(str, numerator)))
        else:
            self.numerator = numerator

        if isinstance(denominator, list):
            self.denominator = int(''.join(map(str, denominator)))
        else:
            self.denominator = denominator

        self._reduce()

    def _reduce(self):
        """Сокращает дробь."""
        common_divisor = gcd(self.numerator, self.denominator)
        self.numerator //= common_divisor
        self.denominator //= common_divisor

    def __add__(self, other):
        """Сложение дробей."""
        new_numerator = self.numerator * other.denominator + other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return BigFraction(new_numerator, new_denominator)

    def __sub__(self, other):
        """Вычитание дробей."""
        new_numerator = self.numerator * other.denominator - other.numerator * self.denominator
        new_denominator = self.denominator * other.denominator
        return BigFraction(new_numerator, new_denominator)

    def __mul__(self, other):
        """Умножение дробей."""
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        return BigFraction(new_numerator, new_denominator)

    def __truediv__(self, other):
        """Деление дробей."""
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        return BigFraction(new_numerator, new_denominator)

    def whole_part(self):
        """Выделение целой части."""
        return self.numerator // self.denominator

    def to_list(self):
        """Представление числителя и знаменателя в виде списков цифр."""
        return ([int(d) for d in str(self.numerator)], [int(d) for d in str(self.denominator)])

    def __lt__(self, other):
        """Меньше ли эта дробь другой?"""
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __eq__(self, other):
        """Равны ли дроби?"""
        return self.numerator * other.denominator == other.numerator * self.denominator

    def __repr__(self):
        return f"{self.numerator}/{self.denominator}"

fractions = [
    BigFraction([1, 2, 3], [4, 5, 6]),
    BigFraction([9, 8, 7], [6, 5, 4]),
    BigFraction([1, 0, 1], [3, 0])
]

min_fraction = min(fractions)
max_fraction = max(fractions)
difference = max_fraction - min_fraction

print(f"Минимальная дробь: {min_fraction}")
print(f"Максимальная дробь: {max_fraction}")
print(f"Разность: {difference}")
