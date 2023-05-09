import calendar

# The number 2 specifies the length of the headers shown
print(calendar.weekheader(3))

print()

print(calendar.firstweekday())
print()

print(calendar.month(2020,7,3))
print(calendar.monthcalendar(2020,7)) # the days are in order but this is a 2D array representing it
print()

print(calendar.calendar(2020))

day_of_week= calendar.weekday(2020,7,9)
print(day_of_week)
print()

is_leap = calendar.isleap((2020))
print(is_leap)
print()

how_leap_days = calendar.leapdays(2000,2021) # if you want to include 2020 you need to go a year higher
print(how_leap_days)
