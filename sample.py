#!/bin/env python

from mortgage.Mortgage import Mortgage

from mortgage import TermScheduler

import datetime

# def __init__(self, house_price, interest, downpayment, schedule):
start_date = datetime.date(2012, 1, 1)
m = Mortgage(300000, 0.035, 300000 * 0.2, TermScheduler.monthly_schedule(start_date, 15, step=1))

principal, interest = 0, 0

for p in m.payments():
    principal += p.principal
    interest += p.interest
    print(p)

print("Total paid {0:.2f} principal and {1:.2f} interest".format(principal, interest))
