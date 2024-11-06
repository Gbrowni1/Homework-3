# Grant Browning
# UWYO COSC 1010
# Submission Date: 11/05/24
# HW 03
# Lab Section: Austin
# Sources, people worked with, help given to: Kyle Rohn(Colorado friend)

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_in_month = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def get_day_of_week(date_input):
    #close to first day of gregorian calendar

    month = 0
    day = 0
    year = 0
    date = {"MM" : month, "DD" : day, "YYYY" : year}
    days_away = 0

   
    def split_the_date():
        """Gather user inputted date and split into a list"""
        date_input = input("Please enter the date you would like to know the day of the week for in MM/DD/YYYY format:")
        for date in date_input:
            month, day, year = date_input.split("/")
            
            #convert values to integers
            month = int(month)
            day = int(day)
            year = int(year)

    def leapyear_test(year):
        """Checks if input year is a leap year"""
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                return False
        return False

    #adjustment if it is a leap year
    if leapyear_test(year):
        days_in_month[2] = 29

    y = year -1

    day = (36 + y + (y/4) - (y/100) + (y/400))%7 # +mon_offset + day_offset then %7

x = 0
if x==0:
    verb = "was"
else:
    verb = "is"


#Example output: 02/21/2022 Monday, or 02/29/2023 Invalid Date
date_input = input("Please enter the date you would like to know the day of the week for in MM/DD/YYYY format:")
weekday = get_day_of_week(date_input)
print(f"{date_input} {verb} a {weekday}")
