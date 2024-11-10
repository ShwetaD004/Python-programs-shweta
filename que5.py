year=int(input("Enter year to check lewp year or not: "))
if year%4==0:
    print(year," is leap year.")
elif year%100==0:
    if year%400==0:
        print(year,"is leap year.")
else:
    print(year,"is not a leap year.")