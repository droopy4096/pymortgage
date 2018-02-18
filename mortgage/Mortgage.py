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
    _payment_periods = None

    def __init__(self, house_price, term, interest, downplayment, start_date,
                 payment_periods=12):
        self._term = term
        self._house_price = house_price
        self._downpayment = downplayment
        self._interest = interest
        self._start_date = start_date
        self._payment_periods = payment_periods

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
        return 1. + self._interest / self._payment_periods

    @property
    def loan_periods(self):
        return self._term

    @property
    def period_payment(self):
        """ Periodic payment sum:
            how much is the payment per period"""
        # https://www.wikihow.com/Calculate-Mortgage-Payments
        p_interest=self.interest/self._payment_periods
        pre_amt = self.principal*(p_interest*(1+p_interest)**self.loan_periods)/((1+p_interest)**self.loan_periods-1)
        ##ORIG pre_amt = float(self.principal) * self.interest / (float(self._payment_periods) * (1. - (1. / self.period_growth) ** self.loan_periods))
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
        # while True:
        for payment_period in xrange(1, self._term+1):
            interest_unrounded = current_balance * interest_decimal * decimal.Decimal(1) / self._payment_periods
            paid_interest = dollar(interest_unrounded, round=decimal.ROUND_HALF_UP)
            full_payment = self.period_payment + self.period_prepayment(payment_period)
            paid_principal = full_payment - paid_interest
            if full_payment >= current_balance + paid_interest:
                yield PeriodMortgage(current_balance, paid_interest, payment_period, 0)
                # yield balance, interest
                break
            current_balance -= paid_principal
            yield PeriodMortgage(paid_principal, paid_interest, payment_period, current_balance)
