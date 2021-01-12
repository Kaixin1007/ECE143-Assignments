import calendar
def number_of_days(year,month):
    '''
    :param year: year
    :param month: month
    :return:the number of calendar days in a given year and month
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert year >0
    assert month >= 1 and month <= 12
    a,res = calendar.monthrange(year, month)
    return res

def number_of_leap_years(year1,year2):
    '''
    :param year1: year1
    :param year2: year2
    :return:the number of leap-years between (including both endpoints) two given years
    '''
    assert isinstance(year1, int)
    assert isinstance(year1, int)
    assert year1 > 0 and year2 > 0
    assert year2 >= year1
    res = calendar.leapdays(year1, year2+1)
    return res

def get_day_of_week(year,month,day):
    '''
    :param year: year
    :param month: month
    :param day: day
    :return: find the string name (e.g., Monday, Tuesday) of the day of the week on a given month,day, and year
    '''
    assert isinstance(year, int)
    assert isinstance(month, int)
    assert isinstance(day, int)
    assert year > 0
    assert month >= 1 and month <= 12
    assert day >= 1 and day <= 31
    name = ['Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday']
    res = calendar.weekday(year, month, day)
    return name[res]

