#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    def load_cargo(self, weight):
        if self.cargo + weight <= self.capacity:
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))


if __name__ == '__main__':
    black_pearl = Ship("Black Pearl", 800)
    black_pearl.name_captain("Jack Sparrow")
    print(black_pearl.captain)
    black_pearl.load_cargo(600)
    black_pearl.unload_cargo(400)
    black_pearl.load_cargo(700)
    black_pearl.unload_cargo(300)
