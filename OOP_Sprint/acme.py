#!/usr/bin/env python

import random


class Product:

    def __init__(self, name, price=10,
                 weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):

        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        stealability = self.price/self.weight
        if stealability < 0.5:
            return 'Not so stealable'
        elif (stealability >= 10) and (stealability < 50):
            return 'Kinda stealable'
        else:
            return 'Very stealable!'

    def explode(self):
        explode = self.flammability * self.weight
        if explode < 10:
            return '...fizzle'
        elif (explode >= 10) and (explode < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):

    def __init__(self, name, price=10,
                 weight=10, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        super().__init__(name=name, weight=weight)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return 'That tickles'
        elif (self.weight >= 5) and (self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
