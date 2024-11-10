Employee={"Name":"John","Age":32,"Salary":50000}
print(type(Employee))
print("Printing Employee Data: ")
print(Employee)

d1={"Name":"Shweta"}
print(d1)
print("Dict. after clear():")
d1.clear()
print(d1)

print("Copy() of dictionary: ")
original={1:"Shravani",2:"Shweta"}
print(original)
new= original.copy()
print(new)
print("get() from dictionary: ")
print(original.get(2))

print("items() from dictionary: ")
print(original.items())