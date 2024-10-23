# given datetime a datetime object should be created
 
import pytest
from src.exceptions.date_validation_exceptions import InvalidDateException
from src.models.datetime import Datetime

def test_if_datetime_object_validates_year_field():
    
    with pytest.raises(InvalidDateException) as excinfo:  
        test_datetime = Datetime(
            day=1,
            month=10,
            year=2010
        )
    assert str(excinfo.value) == "Invalid year provided | year - -1"  
    
def test_if_datetime_object_validates_day_field():
    
    with pytest.raises(InvalidDateException) as excinfo:  
        test_datetime = Datetime(
            day=40,
            month=10,
            year=2012
        )
    assert str(excinfo.value) == "Invalid day provided | day - 40"  

def test_if_datetime_object_validates_month_field():
    
    with pytest.raises(InvalidDateException) as excinfo:  
        test_datetime = Datetime(
            day=4,
            month=40,
            year=2012
        )
    assert str(excinfo.value) == "Invalid month provided | month - 40"      
        