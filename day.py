#!/usr/bin/python3

def day_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        return "th"
    return ["st", "nd", "rd"][day % 10 - 1]

month_days = {
    "January": 31,
    "February":28,
    "March": 31,
    "April": 30,
    "May": 31,
    "June": 30,
    "July": 31,
    "August": 31,
    "September": 30,
    "October": 31,
    "November": 30,
    "December": 31
}

days_of_week = (
    "Sunday",
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday"
)

first_day_2021 = "Friday"

day_number = 366
while day_number > 365:
    day_number = int(input("Enter day number in year > "))
    if day_number > 365:
        print("Day number must be between 1 and 365 inclusive.\nPlease try again...\n")

cumul_days = 0
for key, value in month_days.items():
    cumul_days += value
    if day_number <= cumul_days:
        month = key
        day_of_month = day_number - (cumul_days - value)
        break

day_of_week = (day_number + days_of_week.index(first_day_2021) - 1) % 7 

print(days_of_week[day_of_week]+",", str(day_of_month)+day_suffix(day_of_month), month)

