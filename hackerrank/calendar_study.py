import calendar

#print (calendar.TextCalendar(firstweekday=6).formatyear(2017))
date = input()
month, day, year = map(int, date.split())
weekday_dict = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}
print (weekday_dict[calendar.weekday(year, month, day)])