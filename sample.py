#!/bin/env python

from mortgage.Mortgage import Mortgage

m = Mortgage(300000, 12 * 30, 0.035, 300000 * 0.2, '2002 whatever', 12)

principal, interest = 0, 0

for p in m.statements():
    principal += p.principal
    interest += p.interest
    print p

print "Total paid {0:.2f} principal and {1:.2f} interest".format(principal, interest)
