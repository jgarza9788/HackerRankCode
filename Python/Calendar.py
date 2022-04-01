#https://www.hackerrank.com/challenges/calendar-module/problem

import calendar


i = input()
i = i.split(' ')
date = calendar.datetime.date(year=int(i[2]),month=int(i[0]),day=int(i[1]))
print(calendar.day_name[date.weekday()].upper())