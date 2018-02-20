#!/bin/env python

class Expense(object):
    """Represent expenses during various stages of mortgage process"""
    def __init__(self, title, cost):
        self._title=title
        self._cost=cost

    def __str__(self):
        return "{0}: {1:.2f}".format(self._title, self._cost)
    
    @property
    def title(self):
        return self._title

    @property
    def cost(self):
        return self._cost