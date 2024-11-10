#set functions: 1.add,2.clear(),3.copy
s = set()
print("Type of s is ",type(s))

set1={1,"shweta",2,3.14}
print(set1)
print("Adding element in set")
set1.add("shravani")
print(set1)
print("Removing the set elements: ")
print(set1.clear())

print("Copy set: ")
fruits={"apple","banana","mango"}
print(fruits)
f=fruits.copy()
print(f)

animals={"cat","dog","cow"}
print(animals)