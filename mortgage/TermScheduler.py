import datetime
# from future import print_statement

class WrongSchedule(Exception):
    def __init__(self, exception_txt):
        self.msg=exception_txt

    def __str__(self):
        return self.msg

class TermSchedule(object):
    """Term schedule"""
    def __init__(self,start_date,end_date):
        self.start_date=start_date
        self.end_date=end_date
        self.current_date=self.start_date
        self.next_year=self._plus_year(self.start_date)
        self._annual_periods=None

    def _plus_year(self, from_year, years=1):
        """Caveat: do not use for Feb 29 - won't work as expected"""
        return datetime.date(from_year.year+years, from_year.month, from_year.day)

    def next_term(self, from_date):
        return from_date+self.get_delta()

    def set_annual_periods(self, periods):
        self._annual_periods=int(periods)

    def get_annual_periods(self):
        return self._annual_periods

    annual_periods=property(fset=set_annual_periods,fget=get_annual_periods)

    def get_delta(self):
        pass

    def __iter__(self):
        return self

    def next(self):
        # next_date=self.start_date+self.get_delta()
        # print self.current_date, self.next_year
        if self.current_date>self.end_date:
            raise StopIteration
        elif self.current_date==self.end_date:
            return_date=self.current_date
            self.current_date=self.next_term(self.current_date)
            return return_date
        else:
            return_date=self.current_date
            next_date=self.next_term(self.current_date)
            if next_date > self.end_date:
                next_date=self.end_date
            if next_date >= self.next_year:
                # self.current_date=self.next_year
                # self.next_year=self._plus_year(self.next_year)
                self.current_date=next_date
                self.next_year=self._plus_year(self.next_year)
            else:
                self.current_date=next_date
            return return_date

class WeeklySchedule(TermSchedule):
    def __init__(self,start_date,end_date,weeks=1):
        super(WeeklySchedule, self).__init__(start_date,end_date)
        self.delta=datetime.timedelta(weeks=weeks)
        if 52 % weeks != 0:
            raise WrongSchedule("Schedule does not fit into annual cycle: {0}wk annual {1}wk period".format(52, weeks))
        self.annual_periods=52//weeks

    def get_delta(self):
        return self.delta

class MonthlySchedule(TermSchedule):
    def __init__(self,start_date,end_date,months=1):
        super(MonthlySchedule, self).__init__(start_date,end_date)
        self.months=months
        if 12 % months != 0:
            raise WrongSchedule("Schedule does not fit into annual cycle: {0}mo annual {1}mo period".format(12, months))
        self.annual_periods=12//months

    def next_term(self, from_date):
        next_year=from_date.year
        next_month=from_date.month+self.months
        next_day=from_date.day
        next_year=next_year+next_month//12
        next_month=next_month%12
        return datetime.date(next_year, next_month, next_day)

if __name__ == '__main__':
    ws=WeeklySchedule(start_date=datetime.date(2002,1,1),end_date=datetime.date(2004,3,3),weeks=3)
    ms=MonthlySchedule(start_date=datetime.date(2002,1,1),end_date=datetime.date(2006,3,3),months=2)
