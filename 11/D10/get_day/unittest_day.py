import datetimeexc

def test1():
    day_wanted = datetimeexc.days_want("2021-12-08,Wed, 10:00")
    assert day_wanted == 'Saturday'

def test2():
    day_wanted = datetimeexc.days_want("1970-12-08,Wed, 11:00")
    assert day_wanted == 'Friday'

if __name__ == '__main__':
    test2()