#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное число, левая граница диапазона;
поле second — дробное число, правая граница диапазона.
Реализовать метод rangecheck() — проверку заданного числа
на принадлежность диапазону.
"""


class Number:

    def __init__(self, first=0.0, second=0.0):
        try:
            self.__first = float(first)
            self.__second = float(second)
        except ValueError:
            ValueError("Проверьте правильность ввода!")

    @property
    def first(self):
        return self.__first

    @property
    def second(self):
        return self.__second

    def read(self):
        lower_bound = float(input("Введите левую границу диапазона: "))
        upper_bound = float(input("Введите правую границу диапазона: "))
        if isinstance(lower_bound, float) and (isinstance(upper_bound, float)):
            self.__first = float(lower_bound)
            self.__second = float(upper_bound)
        else:
            raise ValueError("Проверьте введенные границы диапазона!")

    def display(self):
        print(f"1: {self.first}")
        print(f"2: {self.second}")

    def rangecheck(self, number=None):
        if self.first > self.second:
            raise ValueError("Введенная левая граница больше правой!")
        if isinstance(number, float) or isinstance(number, int):
            pass
        else:
            try:
                number = float(input("Задайте число: "))
            except ValueError:
                ValueError("Введено не число!")
        if self.first <= float(number) <= self.second:
            print(f"Число {number} в диапазоне [{self.first}, {self.second}]")
        else:
            print(f"Число {number} не в [{self.first}, {self.second}]")


if __name__ == "__main__":
    test = Number()
    test.read()
    test.display()
    test.rangecheck()
    test.rangecheck(23.2)
