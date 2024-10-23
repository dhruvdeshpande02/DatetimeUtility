
import pytest
from src.exceptions.date_validation_exceptions import InvalidDateException
from src.models.datetime import Datetime


def test_if_datetime_object_validates_leap_year():
    test_datetime = Datetime(day=29, month=2, year=2020)
    assert test_datetime.day == 29

    with pytest.raises(InvalidDateException) as excinfo:
        test_datetime = Datetime(day=29, month=2, year=2019)
    assert str(excinfo.value) == "Invalid day provided for February | day - 29"
