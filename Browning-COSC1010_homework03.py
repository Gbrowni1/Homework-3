# Grant Browning
# UWYO COSC 1010
# Submission Date: 11/05/24
# HW 03
# Lab Section: Austin
# Sources, people worked with, help given to: Kyle Rohn(Colorado friend CompSci Major)
# Comments:

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_in_month = {0:0, 1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def get_day_of_week(date_input):
    """Gets day of the week from user inputted date, in MM/DD/YYYY format. Also checks for incorrect inputs."""
    month = 0
    day = 0
    year = 0
    date = {"MM" : month, "DD" : day, "YYYY" : year}
    days_away = 0

    def split_the_date():
        """Gather user inputted date and split into a list"""

        month, day, year = date_input.split("/")
        #convert values to integers
        month = int(month)
        day = int(day)
        year = int(year)
        return month, day, year
    
    def is_proper_format(format):
        """Checks all error input parameters to give green light to print statement, and outputs corresponding error message to improper inputs."""
        if len(month)==2 and len(day)==2 and len(year)==4:
            if month>0 and day>0 and year>0:
                if month.isalpha()==False and day.isalpha()==False and year.isalpha()==False:
                    if month < 1 or month > 12 or day < 1 or day > 31:
                            if date_input.isalpha==False:
                                return True
                            return False
                    return False
                return False
            return False
        return False

    if is_proper_format==False:
        check = 1
        print("Improper format. Please enter date in MM/DD/YYYY format.")
        return check
    
    month, day, year = split_the_date()



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
    month_offset = 0
    for MM in range(month):
        month_offset += days_in_month[MM]

    day_offset = day - 1

    day = (36 + y + (y//4) - (y//100) + (y//400) + month_offset + day_offset) %7 # +mon_offset + day_offset then %7

    return day   
        
#Example output: 02/21/2022 Monday, or 02/29/2023 Invalid Date
while True:
    date_input = input("Please enter the date you would like to know the day of the week for in MM/DD/YYYY format:")

    check = get_day_of_week(date_input) 

    if check==1:
        print("Improper format. Please enter date in MM/DD/YYYY format.")
    if date_input.upper=="EXIT":
        break
    else:
        weekday_num = get_day_of_week(date_input)
        weekday = days_of_week[weekday_num]
        print(f"{date_input} is a {weekday}")

