import datetime
year1 = int(input("Input start year: "))
month1 = int(input("Input start month: "))
day1 = int(input("Input start day: "))
date1 = datetime.date(year1, month1, day1)

year2 = int(input("Input end year: "))
month2 = int(input("Input end month: "))
day2 = int(input("Input end day: "))
date2 = datetime.date(year2, month2, day2)

print("Start date: ", date1) 
print("End date: ", date2)
difference = date2 - date1
print(difference.day)
