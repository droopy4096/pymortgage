# coding=UTF-8

import decimal
from PeriodMortgage import PeriodMortgage

DOLLAR_QUANTIZE = decimal.Decimal('.01')


def dollar(f, round=decimal.ROUND_CEILING):
    """
    This function rounds the passed float to 2 decimal places.
    """
    if not isinstance(f, decimal.Decimal):
        f = decimal.Decimal(str(f))
    return f.quantize(DOLLAR_QUANTIZE, rounding=round)


class Mortgage(object):

    _term = None   # payment_per_year * years
    _house_price = None
    _downpayment = None
    _interest = None
    _start_date = None
    _annual_payment_periods = None

    def __init__(self, house_price, term, interest, downpayment, schedule,
                 annual_payment_periods=12):
        """
        @param decimal house_price
        @param int term
        @param decimal interest
        @param decimal downplayment
        @param TermSchedule schedule
        @param int payment_periods
        """
        self._term = term
        self._house_price = house_price
        self._downpayment = downpayment
        self._interest = interest
        self._start_date = schedule
        self._annual_payment_periods = annual_payment_periods

        ### self._annual_payment_periods=schedule.annual_periods
        ### self._schedule=list(schedule)
        ### self._term=len(self._schedule)
        # self._term=

    def period_prepayment(self, period):
        """
         abstract function/hook for prepayment oranization

        @param int period :
        @return float :
        @author
        """
        return 0
        # raise NotImplemented

    @property
    def period_growth(self):
        return 1. + self._interest / self._annual_payment_periods

    @property
    def loan_periods(self):
        return self._term

    @property
    def period_payment(self):
        """ Periodic payment sum:
            how much is the payment per period"""
        # https://www.wikihow.com/Calculate-Mortgage-Payments
        p_interest = self.interest / self._annual_payment_periods
        pre_amt = self.principal * (p_interest * (1 + p_interest) **
                                    self.loan_periods) / ((1 + p_interest)**self.loan_periods - 1)
        return dollar(pre_amt, round=decimal.ROUND_CEILING)

    @property
    def interest(self):
        return self._interest

    @property
    def principal(self):
        """ Principal borrowed """
        return self._house_price - self._downpayment

    def payments(self):
        """
         iterator function

        @return MontlyMortgage :
        @author
        """
        current_balance = dollar(self.principal)
        interest_decimal = decimal.Decimal(str(self.interest)).quantize(decimal.Decimal('.000001'))
        for payment_period in xrange(1, self._term + 1):
            interest_unrounded = current_balance * interest_decimal * \
                decimal.Decimal(1) / self._annual_payment_periods
            paid_interest = dollar(interest_unrounded, round=decimal.ROUND_HALF_UP)
            full_payment = self.period_payment + self.period_prepayment(payment_period)
            paid_principal = full_payment - paid_interest
            if full_payment >= current_balance + paid_interest:
                yield PeriodMortgage(current_balance, paid_interest, payment_period, 0)
                # yield balance, interest
                break
            current_balance -= paid_principal
            yield PeriodMortgage(paid_principal, paid_interest, payment_period, current_balance)

if __name__=='__main__':
    from datetime import date
    m = Mortgage(300000, 12 * 30, 0.035, 300000 * 0.2, date(2009,10,1), 12)

    principal, interest = 0, 0

    for p in m.payments():
        principal += p.principal
        interest += p.interest
        print(p)

    print("Total paid {0:.2f} principal and {1:.2f} interest".format(principal, interest))