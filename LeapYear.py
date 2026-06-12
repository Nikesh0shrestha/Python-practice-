# program to check the given year is leap year or not

year = int(input("Enter the year :"))

if (year % 400 == 0) and (year % 1000 == 0):
    print( year,"is a leap year.")
elif (year % 4 == 0) and (year % 100 != 0):
    print(year,"is a leap year.")
else:
    print(year, "is a not a leap year.")
