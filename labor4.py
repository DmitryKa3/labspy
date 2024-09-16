import datetime

n= datetime.date(2024,9,11)
print(n)

def funciton(n):
    firstday = datetime.datetime(n.year, n.month, 1)
    firstweek = firstday.weekday()
    if firstweek <= 2:
        sreda = firstday + datetime.timedelta(days=2 - firstweek + 14)
    else:
        sreda = firstday + datetime.timedelta(days=2 - firstweek + 21)
    return  sreda

print(funciton(n))