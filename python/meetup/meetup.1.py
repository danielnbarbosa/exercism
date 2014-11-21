from datetime import date
import calendar


def meetup_day(year, month, day, which):
    list = []
    for i in range(1,calendar.monthrange(year, month)[1] + 1):
        d = date(year, month, i)
        if d.strftime("%A") == day:
            list.append(i)
    #print list
    if which == '1st':
        ans = list[0]
    elif which == '2nd':
        ans = list[1]
    elif which == '3rd':
        ans = list[2]
    elif which == '4th':
        ans = list[3]
    elif which == 'last':
        ans = list[-1]
    elif which == 'teenth':
        for i in range(13,19):
            d = date(year, month, i)
            if d.strftime("%A") == day:
                ans = i
    
    return date(year, month, ans)
