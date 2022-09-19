import pytest
from datetime import datetime as dt



def test_time_now(datetime_now):
    assert "PM" in dt.strftime(datetime_now, "%I:%M %p  %S sec"), "Sorry, but it's ante meridiem!"


@pytest.mark.usefixtures('even_10to1', 'odd_10to1')
class Test_Even_10to1():

    count = 0

    @pytest.mark.order(1)
    def test_is_even(self, even_10to1):
        self.__class__.count += 1
        print(f'\nNumber of times a method of this class was called: {self.count}')
        print(f'{even_10to1=}')
        assert not(even_10to1 % 2), "Sorry, it must be an even number between 10-1"

    @pytest.mark.order(2)
    def test_is_odd(self, odd_10to1):
        type(self).count += 1
        print(f'\nNumber of times a method of this class was called: {self.count}')
        print(f'{odd_10to1=}')
        assert not odd_10to1 % 2, "క్షమించాలి, ఇది 10-1 మధ్యలోని బేసిసంఖ్య అయివుండాలి"

    @pytest.mark.order(3)
    def test_is_evenodd(self, even_10to1, odd_10to1):
        Test_Even_10to1.count += 1
        print(f'\nNumber of times a method of this class was called: {self.count}')
        print(f'{even_10to1  +  odd_10to1 = }')
        assert (even_10to1 + odd_10to1) % 2, "Sorry, it must be an even number between 10-1"