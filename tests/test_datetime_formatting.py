from src.models.datetime import Datetime


def test_datetime_object_return_correct_dd_mm_yy_format():
    test_datetime = Datetime(
        day=1,
        month=10,
        year=2016
    )
    assert "1/10/16"==test_datetime.get_dd_mm_yy_format()