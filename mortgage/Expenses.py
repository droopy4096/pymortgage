#!/bin/env python


class Expense(object):
    """Represent expenses during various stages of mortgage process"""

    def __init__(self, title, cost, expense_date):
        self._title = title
        self._cost = cost
        self._date = expense_date

    def __str__(self):
        return "{0}: {1:.2f}".format(self._title, self._cost)

    @property
    def title(self):
        return self._title

    @property
    def cost(self):
        return self._cost

    @property
    def date(self):
        return self._date


class ExpenseList(object):
    def __init__(self, **kwargs):
        self._expenses = []
        if kwargs:
            self._options = kwargs
        else:
            self._options = {}

    def addExpense(self, expense):
        self._expenses.append(expense)

    def sum(self):
        return sum([e.cost for e in self._expenses])

    def __str__(self):
        return "{0}\nTotal: {1:.2f}".format(
            str([("{0} ({1})".format(e.title, e.date), e.cost) for e in self._expenses]), self.sum())

    @property
    def options(self):
        """return expenseList options"""
        return self._options


class Fee(Expense):
    def __init__(self, title, cost, expense_date):
        super(Fee, self).__init__(title, cost, expense_date)

    def penalty(self, fee_date):
        return 0


if __name__ == '__main__':
    import datetime
    el = ExpenseList()
    el.addExpense(Expense('closing cost', 10000, datetime.date(2009, 11, 2)))
    el.addExpense(Expense('Title Insurance', 1000, datetime.date(2009, 11, 4)))
    print(el)
