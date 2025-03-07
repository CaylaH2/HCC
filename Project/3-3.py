#Declared Variables
year = 0
month = 0
day = 0

#input statements
month = int(input("Enter month: "))
day = int(input("Enter day: "))
year = int(input("Enter year: "))

#Check for leap year (February only!)
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0 ) or (year % 400 == 0)

#Days per month
if month == 2:
    max_days = 29 if is_leap_year(year) else 28
elif month in {4, 6, 9, 11}:
    max_days = 30
elif month in {1, 3, 5, 7, 8, 10, 12}:
    max_days = 31
else:
    max_days = 0

#Running input data
if year > 0 and (1 <= month <= 12) and (1 <= day <= max_days):
    print(f"{month}/{day}/{year} is a valid date.")
else:
    print(f"{month}/{day}/{year} is an invalid date.")