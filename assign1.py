#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Winter 2024
Author: Rina An
Student Number: 102664224
Student ID: yan28
Course: OPS445NCC
'''

import sys

def usage():
    """This is the usage of the script"""

    print("Usage: assign1.py DD-MM-YYYY N")
    
def days_in_mon(month, year):
    """It is the total number of days of each month."""

    if leap_year(year) == "True":
        feb_maximum = 29
    else:
        feb_maximum = 28
    
    months_of_the_year = {
        1: 31, 2: feb_maximum,
        3:31, 4:30, 5:31, 6:30, 7:31,
        8:31, 9:30, 10:31, 11:30, 12:31}
    
    return months_of_the_year[month]


def valid_date(date):
    """This is for checking a valide date of the given date."""

    if len(date) != 10:
        print("Error: wrong date entered")
        return False
    else:
        str_day, str_month, str_year = date.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)  

        if month < 1 or month > 12:
            print("Error: wrong month entered")
            return False
        
        days_max = days_in_mon(month,year)

        if day > days_max:
            print("Error: wrong day entered")
            return False
    
        return True
        
def leap_year(year):
    """takes a year in YYYY format, and returns True if it's a leap year, False otherwise."""

    if year % 4 == 0:
        feb_max = 29
    else:
        feb_max = 28

    if year % 100 == 0:
        feb_max = 29
    
    if feb_max == 29:
        return True
    else:
        return False
    
def after(today):
    """after takes a valid date string in DD-MM-YYYY format and returns"""
    """a date string for the next day in DD-MM-YYYY format."""

    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        lyear = year % 4 # TODO: put this into the function leap_year.
        if lyear == 0:
            feb_maximum = 29 # this is a leap year
        else:
            feb_maximum = 28 # this is not a leap year

        lyear = year % 100
        if lyear == 0:
            feb_maximum = 28 # this is not a leap year

        lyear = year % 400
        if lyear == 0:
            feb_maximum = 29 # this is a leap year

        tmp_day = day + 1 # next day

        mon_max = {
            1:31, 2:feb_maximum, 3:31,
            4:30, 5:31, 6:30, 7:31, 8:31,
            9:30, 10:31, 11:30, 12:31}
        if tmp_day > mon_max[month]:
            to_day = tmp_day % mon_max[month]
            # if tmp_day > this month's max, reset to 1
            tmp_month = month + 1
        else:
            to_day = tmp_day
            tmp_month = month + 0

        if tmp_month > 12:
            to_month = 1
            year = year + 1
        else:
            to_month = tmp_month + 0

        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)
        return next_date

def before(today):
    """It will returns a date fron the previous date."""
    """a date string for the previous day in DD-MM-YYYY format."""

    if len(today) != 10:
        return '00-00-0000'
    else:
        str_day, str_month, str_year = today.split('-')
        year = int(str_year)
        month = int(str_month)
        day = int(str_day)

        tmp_day = day - 1 # previous day
        tmp_month = month
        tmp_year = year

        if tmp_day == 0:
            tmp_month = month - 1
            if tmp_month == 0:
                tmp_month = 12
                tmp_year = year -1
            else:
                tmp_day = days_in_mon(tmp_month, tmp_year)
        
        previous_date = str(tmp_day).zfill(2)+"-"+str(tmp_month).zfill(2)+"-"+str(year)

        return previous_date

def dbda(start_date, num_days):
    """It will returns a date for either next and previous day the given date."""
    
    end_date = 0
    end_date = start_date

    if int(num_days) >= 0:
        for day in range(num_days):
            end_date = after(end_date)    
    else:
        for day in range(num_days):
            end_date = before(end_date)

    
    return end_date

if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: assign1.py DD-MM-YYYY N")
        exit()

    date = str(sys.argv[1])
    num_days = int(sys.argv[2])

    if valid_date(date):
        result = dbda(date, num_days)
        print(result)