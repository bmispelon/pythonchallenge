# http://www.pythonchallenge.com/pc/return/uzi.html
# This problem starts with a picture of a calendar for the month of january
# of the year 1XX6.
# We know that january 26th of that year is a monday, and also that it is a leap year.
# The hints also tells us that we're to find the second most recent year that matches these criteria.
# January 27th of that year is the birth date of a famous person.
# Their name is the solution to the problem.
from calendar import isleap
from datetime import date

if __name__ == '__main__':
    def matches_criteria(year):
        return all([
                    str(year).startswith('1'),
                    str(year).endswith('6'),
                    isleap(year),
                    date(year=year, month=1, day=26).weekday() == 0,
        ])
    possible_years = filter(matches_criteria, range(1, 2012))
    
    print possible_years[-2]
