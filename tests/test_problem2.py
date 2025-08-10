from problem2.problem2 import date_format


def test_date_format():
    # pass
    assert date_format('07/04/2021') == '2021-07-04'


def test_date_format2():
    # pass
    assert date_format('11/31/1986') == '1986-11-31'

test_date_format2()