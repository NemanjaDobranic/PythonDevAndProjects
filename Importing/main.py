import datetime

print('Min year in this library is',datetime.MINYEAR)
print('Max year in this library is',datetime.MAXYEAR)

print("Today's date",datetime.date.today())

#Class Date
date = datetime.date(2018,9,8)
print('Date',date)

#different formats
print('Different date formats')
print(date.strftime("%d/%m/%Y"))
print(date.strftime("%d.%m.%y"))
print(date.strftime("%d/%B/%Y"))
print(date.strftime("%b-%d-%Y"))

print('Weekday:',datetime.date.weekday(datetime.date.today()))

#Class Time
time = datetime.time(15,45,12)
print('Time',time)

now = datetime.datetime.now()
print('Different time formats')
print(now.strftime("%c")) #%c - local date and time
print(now.strftime("%x")) #%x-local's date
print(now.strftime("%X")) #%X- local's time
print(now.strftime("%H:%M%S")) #24 Hour format
print(now.strftime("%I:%M:%S %p")) #12 Hour Format

#Throws error minute must be in 0..59
#time = datetime.time(12,75,12)
#print('Time',time)

#Class DateTime
datetime1 = datetime.datetime(2018,11,12,11,12,25)
print('Date and time',datetime1)

#Class Timedelta
delta = datetime.timedelta(
     days=365,
     hours=12,
     weeks=2
)
print('Now:',now)
print('Delta:',delta)
print('Delta added to now:',now+delta)
print('Delta subtracted from now:',now-delta)
print('Delta between tow dates:',now-datetime1)

print('UTC now:',datetime.datetime.utcnow())