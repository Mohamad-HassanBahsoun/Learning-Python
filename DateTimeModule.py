# calculate the difference btw today and your birthday
# or you can makes apps that sendemails automatically based on date
# or you can make an instagram clone that can say things like "posted three days a go"

import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(2002,7,9)
print(birthday)    # it is not a string that returns but a datetime object

since_birth = (today - birthday).days # this will give us the number of days and not a datetime obj
print(since_birth)  # this is the days since i was born

tdelta = datetime.timedelta(days=10)   # this adds 10 days to whatever you would like
print(today+tdelta)

print(today.month)
print(today.day)
print(today.weekday())


print(datetime.time(11,59,20,15))
# datetime.date(Y, M, D)
# datetime(h, m, s, ms)
# datetime(Y, M, D, h, m, s, ms)

hour_delta = datetime.timedelta(hours= 10)
print(datetime.datetime.now()+ hour_delta) # this adds 10 hours to the current day and time

datetime_today = datetime.datetime.now(tz = pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

# this is for all timezones
for tz in pytz.all_timezones:
    print(tz)


# String formatting with dates
# 2020-07-21 --> July 21, 2020
#strftime (f - formatting)

print(datetime_pacific.strftime('%B %d, %Y'))

# 2020-07-21 <-- July 21, 2020
#strptime (p=parsing)

datetime_thing = datetime.datetime.strptime('July 21, 2020','%B %d, %Y')
print(datetime_thing)

# look for maya time thing apparantly its easier