from src.exceptions.date_validation_exceptions import InvalidDateException


class Datetime:
    DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def is_leap_year(self):
        return(self.year % 4 ==0 and self.year % 100 !=0) or (self.year % 400 == 0)

    def count_leap_years(self, start_year, end_year):
        count = 0
        for year in range(start_year, end_year + 1):
            if self.is_leap_year(year):
                count += 1
        return count

    def get_difference_in_days_between_years(self, end_date):
        leap_count = self.count_leap_years(self.year, end_date.year)
        difference_in_years = (end_date.year - self.year) * 365 + leap_count
        return difference_in_years

    def __validate_date(self):
        if self.year<0:
            raise InvalidDateException(message=f'Invalid year provided | year - {self.year}')
        if self.day<1 or self.day>self.DAYS_IN_MONTH[self.month-1]:
            raise InvalidDateException(message=f'Invalid day provided | day - {self.day}')
        if self.month<1 or self.month>12:
            raise InvalidDateException(message=f'Invalid month provided | month - {self.month}')
        if self.is_leap_year() and self.month == 2 and self.day > 29:
            raise InvalidDateException(message=f'Invalid day provided for leap year | day - {self.day}')
        if not self.is_leap_year() and self.month == 2 and self.day >28:
            raise InvalidDateException(message=f'Invalid day provided for month of feb | day - {self.day}')

    def __init__(self,day:int,month:int,year:int):
        self.day = day
        self.month = month
        self.year = year
        self.__validate_date()

    def get_dd_mm_yy_format(self)->str:
        return f"{self.day}/{self.month}/{self.year}"
    
