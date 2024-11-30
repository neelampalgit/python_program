import datetime


#1. Current date time
curr_date_time = datetime.datetime.now()
print(curr_date_time)

#2. Specific date time object
dt = datetime.datetime(2024,11,30,10,20,35)
print(dt)

#3. Accessing the attributes of datetime
print("Year:", curr_date_time.year)
print("month:", curr_date_time.month)
print("day:", curr_date_time.day)
print("hour:", curr_date_time.hour)
print("minute:", curr_date_time.minute)
print("second:", curr_date_time.second)
print("microsecond:", curr_date_time.microsecond)

#4. format datetime object into a string
print(curr_date_time.strftime("%Y/%m/%d %H:%M:%S"))

#5. Custom date format
# %Y - Year with century (2024)
# %m - Month (eg.-11 for Nov, 03 for Mar)
# %d - Day of the month
# %H - hour(24-hr clock)
# %M - Minute
# %S - second
print(curr_date_time.strftime("%A, %B %d, %Y"))

print(type(curr_date_time))

#6. Parse date string into datetime
datestring = "2024-11-30 12:30:45"
dt = datetime.datetime.strptime(datestring,"%Y-%m-%d %H:%M:%S")
print(dt)

#7. Adding days to a datetimeobject
new_date = curr_date_time+datetime.timedelta(days=10)
print("10 days later:", new_date)

#8. Subtracting days to a datetimeobject
new_date = curr_date_time - datetime.timedelta(days=10)
print("10 days ago:", new_date)

#9. Print today's date only
today = datetime.date.today()
print(today)

#10. Specific date object
my_date = datetime.date(2024,12,30)
print(my_date)

#11. Print specific time object
print(datetime.time(12, 30, 45))

# 12. Working with timedelta object
delta = datetime.timedelta(days=5, hours=2, minutes=30)
print(delta)

#13. Adding timedelta to a datetime
now = datetime.datetime.now()
new_time = now+datetime.timedelta(days=10, hours=1)
print(new_time)

#14. Get the current time in UTC
now_utc = datetime.datetime.now(datetime.timezone.utc)
print(now_utc)

#15. specific timezone
tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
now_ist=datetime.datetime.now(tz)
print(now_ist)













