#function of list: 2.copy,3.deepcopy,4.clear and 5.count
import copy
list1=[1,2,3,4,5]
list2=copy.copy(list1)
print(list1)
print("O/P after Copy(): ")
print(list2)

list3=copy.deepcopy(list1)
print(list3)

list4=[10,20,30,10,20,30]
print(list4)
print("O/P after Clear():")
list4.clear()
print(list4)

list5=[20,30,10,80,70,30,50,30]
print(list5)
print("Counting 30 in above list")
print(list5.count(30))