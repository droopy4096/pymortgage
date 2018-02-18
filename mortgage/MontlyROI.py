#!/bin/env python


class MonthlyROI(object):

    _year
    _month
    _mortgage_payment
    _principal_paid
    _interest_paid
    _appreciated_price
    _tax
    _insurance
    _writeoff
    _net_worth_gain
    _appreciated_net_worth_gain
    _rent_equivalent
    _apppreciated_rent_equivalent
    _mortgage

    def __init__(self, year, month,
                 mortgage_payment, principal_paid,
                 interest_paid, appreciated_price,
                 tax, insurance, writeoff, net_worth_gain,
                 appreciated_net_worth_gain, rent_equivalent,
                 appreciated_rent_equivalent, mortgage):
        self._year = year
        self._month = month
        self._mortgage_payment = mortgage_payment
        self._principal_paid = principal_paid
        self._interest_paid = interest_paid
        self._appreciated_price = appreciated_price
        self._tax = tax
        self._insurance = insurance
        self._writeoff = writeoff
        self._net_worth_gain = net_worth_gain
        self._appreciated_net_worth_gain = appreciated_net_worth_gain
        self._rent_equivalent = rent_equivalent
        self._apppreciated_rent_equivalent = appreciated_rent_equivalent
        self._mortgage = mortgage

    def _str_(self):
        """
        @return string :
        @author
        """
        pass

    def header(self):
        """
        @return string :
        @author
        """
        pass
