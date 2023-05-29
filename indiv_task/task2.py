#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime as dt

"""
Создать класс Date для работы с датами в формате «год.месяц.день».
Дата представляется структурой с тремя полями типа unsigned int:
для года, месяца и дня. Класс должен включать не менее трех функций
инициализации: числами, строкой вида «год.месяц.день»
(например, «2004.08.31») и датой. Обязательными операциями являются:
вычисление даты через заданное количество дней,
вычитание заданного количества дней из даты,
определение високосности года, присвоение и получение отдельных частей
(год, месяц, день), сравнение дат (равно, до, после),
вычисление количества дней между датами.
"""


class Date:
    # Конструктор
    def __init__(self, day=1, month=1, year=2000):
        self.__day = int(day)
        self.__month = int(month)
        self.__year = int(year)

    # Свойства (для присвоения и получения отдельных частей)
    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if 1 <= d <= 31:
            self.__day = int(d)
        else:
            raise ValueError

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if 1 <= m <= 12:
            self.__month = int(m)
        else:
            raise ValueError

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        self.__year = int(y)

    # Ввод даты в виде строки -> экземпляр класса
    def read_str(self):
        date_str = input("Введите дату: (ГГГГ.ММ.ДД): ")
        try:
            self.__year, self.__month, self.__day = map(
                int, date_str.split(".")
            )
        except ValueError:
            raise ValueError("Задана строка неверного типа!")

    # Ввод даты числами -> экземпляр класса
    def read_nums(self):
        day = int(input("Введите день: "))
        month = int(input("Введите месяц: "))
        year = int(input("Введите год: "))
        self.__day, self.__month, self.__year = int(day), int(month), int(year)

    # Конвертация даты экземпляра класса -> дата типа datetime
    def dt_from_class(self):
        return dt.date(self.year, self.month, self.day)

    # Вывод даты на экран в формате ДД.ММ.ГГГГ
    def display(self):
        print(f"{self.day}.{self.month}.{self.year}")

    # Проверка. Является ли год високосным?
    def is_leap_year(self):
        if (
            (self.__year % 400 == 0)
            or (self.__year % 100 != 0)
            and (0 == self.__year % 4)
        ):
            return True
        else:
            return False

    # Вычисление даты через заданное количество дней
    def add_days(self, added_days):
        curr_date = self.dt_from_class()
        new_date = curr_date + dt.timedelta(days=added_days)
        return new_date

    # Вычитание заданного количества дней из даты
    def subtract_days(self, removed_days):
        curr_date = self.dt_from_class()
        new_date = curr_date - dt.timedelta(days=removed_days)
        return new_date

    # Сравнение дат (экземпляр класса vs другой экземпляр класса)
    def compare(self, to_compare):
        curr_date = self.dt_from_class()
        date_to_compare = to_compare.dt_from_class()
        if curr_date == date_to_compare:
            print("Даты одинаковы!")
        elif curr_date > date_to_compare:
            print(f"Первая дата {curr_date} больше второй {date_to_compare}.")
        elif curr_date < date_to_compare:
            print(f"Вторая дата {date_to_compare} больше первой {curr_date}.")

    # Вычисление количества дней между датами
    def days_between(self, to_compare):
        curr_date = self.dt_from_class()
        date_to_compare = to_compare.dt_from_class()
        delta = (curr_date - date_to_compare).days
        return delta


if __name__ == "__main__":
    # Установка даты при создании экземпляра класса
    date1 = Date(1, 1, 2002)
    date1.display()
    print("-" * 20)
    # Установка даты вводом строки вида "ГГГГ.ММ.ДД"
    date2 = Date()
    date2.read_str()
    date2.display()
    print("-" * 20)
    # Установка даты вводом чисел по отдельности
    date3 = Date()
    date3.read_nums()
    date3.display()
    print("-" * 20)
    # Установка даты при помощи свойств
    date4 = Date()
    date4.day = 20
    date4.month = 5
    date4.year = 2002
    date4.display()
    print("***" * 20)

    if date1.is_leap_year():
        print(f"Год {date1.year} - високосный!")
    else:
        f"Год {date1.year} не является високосным!"

    print(
        f"Разница между {date2.dt_from_class()} и {date1.dt_from_class()}"
        f" составляет {date2.days_between(date1)} дней."
    )

    date2.compare(date1)
    print(date1.add_days(3))
    print(date1.subtract_days(5))
