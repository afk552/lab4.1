#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class River:
    # список всех рек
    all_rivers = []

    def __init__(self, name, length):
        self.name = name
        self.length = length
        # добавляем текущую реку в список всех рек
        River.all_rivers.append(self)


if __name__ == '__main__':
    volga = River("Волга", 3530)
    seine = River("Сена", 776)
    nile = River("Нил", 6852)
    # далее печатаем все названия рек
    for river in River.all_rivers:
        print(river.name)
