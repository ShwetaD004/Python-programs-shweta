#1.append function of list:
list=[]
n=int(input("Enter the number of elements in list: "))
for i in range(0,n):
    list.append(input("Enter the item: "))
print("Printing list items: ")
for i in list:
    print(i,end=' ')    