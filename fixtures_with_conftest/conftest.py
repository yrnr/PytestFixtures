import pytest
from datetime import datetime as dt


@pytest.fixture
def datetime_now():
    return dt.now()

@pytest.fixture(params=range(10,0,-2), scope='class') # list(params) == [10, 8, 6, 4, 2]
def even_10to1(request):
    return request.param

@pytest.fixture(params=range(9,0,-2), scope='class') # list(params) == [9, 7, 5, 3, 1]
def odd_10to1(request):
    return request.param