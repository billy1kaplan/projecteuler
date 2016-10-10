import sys
import datetime

def countsundays(startyear, endyear):
    count = 0
    for year in range(startyear, endyear + 1):
        for month in range(1, 13):
            if datetime.date(year, month, 1).strftime("%A") == 'Sunday':
                count += 1
    return count

print(countsundays(1901, 2000))
