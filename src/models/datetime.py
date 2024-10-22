from src.exceptions.date_validation_exceptions import InvalidDateException


class Datetime:

    def __validate_date(self):
        if self.year<0:
            raise InvalidDateException(message=f'Invalid year provided | year - {self.year}')
        if self.day<1 or self.day>31:
            pass

    def __init__(self,day:int,month:int,year:int):
        self.day = day
        self.month = month
        self.year = year
        self.__validate_date()

    def get_dd_mm_yy_format(self)->str:
        return f"{self.day}/{self.month}/{self.year%100}"