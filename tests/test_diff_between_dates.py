import pytest
from src.models.datetime import Datetime
from src.exceptions.date_validation_exceptions import InvalidDateException

def test_difference_in_years():
    start_date = Datetime(1, 1, 2000)
    end_date = Datetime(1, 1, 2020)
    assert start_date.get_difference_in_days_between_years(end_date) == 7300  

def test_difference_in_years_invalid_dates():
    with pytest.raises(InvalidDateException):
        Datetime(32, 1, 2000) 