import datetime
def checkfriday(month,year):
    date1=datetime.date(year,month,13)
    return date1.weekday()==4
month=int(input("Enter the month: "))
year=int(input("Enter the year: "))
print(checkfriday(month,year))
