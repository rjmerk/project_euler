"""
You are given the following information, but you may prefer to do some
research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
(1 Jan 1901 to 31 Dec 2000)?
"""
from utils import measure_execution_time

MONTHS_LENGTHS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def main() -> None:
    print("Problem 19")
    with measure_execution_time():
        start_year = 1901
        end_year = 2001
        result = sundays_on_day_of_month(1, start_year, end_year)
    print(f"There are {result} Sundays on the first of the month between {start_year} and {end_year}")


def sundays_on_day_of_month(day_of_month, start_year, end_year):
    assert 1900 <= start_year < end_year
    assert 1 <= day_of_month <= 31
    result = 0
    year = 1900
    day = 7
    while year < end_year:
        month = 1
        month_lengths = MONTHS_LENGTHS
        if is_leap_year(year):
            month_lengths[1] = 29
        while month < 13:
            if day == day_of_month and year >= start_year:
                result += 1
            day += 7
            if day > month_lengths[month - 1]:
                day -= month_lengths[month - 1]
                month += 1
        year += 1
    return result


def is_leap_year(year):
    if year % 100 == 0 and not year % 400 == 0:
        return False
    else:
        return year % 4 == 0


if __name__ == '__main__':
    main()
