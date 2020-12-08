#!/bin/env python

from mortgage.Mortgage import Mortgage

from mortgage import TermScheduler
import json

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

from mortgage.ROI import ROI

roi=ROI( mortgage=m, 
         target_sell_price=320000, 
         appreciation=0.002, 
         baseline_return=300000, 
         investments=5000, 
         property_tax_rate=0.01, 
         property_insurance=2000, 
         tax_rate=0.3, 
         sale_expences=0.1)
roi_list=[]
for r in roi():
    roi_list.append(r.serialize_json())

print(json.dumps(roi_list, indent=2))