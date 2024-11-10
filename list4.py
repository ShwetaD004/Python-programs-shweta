#functions in list: 6.extend,7.index.8.pop,9.remove
fruits1=["mango","apple","jackfruit"]
fruits2=["jamun","banana"]
print(fruits1)
print(fruits2)
print("O/P after extend(): ")
fruits1.extend(fruits2)
print(fruits1)

print("Find position using index(): ")
animals= ["cat", "dog", "tiger"]
print(animals)
# searching positiion of dog
print(animals.index("dog"))

print("Popping element from list:")
animals.pop()
print(animals)

print("Removing element 2 from list: ")
list1=[1,2,3,4,5]
print(list1)
list1.remove(2)
print(list1)