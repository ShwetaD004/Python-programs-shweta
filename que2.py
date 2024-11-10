#find largest of two numbers:
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))

if a>b and a>c:
    print("%d is greatest number."%a)
elif b>a and b>c:
    print("%d is greatest number."%b)
else:
    print("%d is greatest number."%c)