file= open ('exp1.txt','r')
print("Open file: ")
print(file.read())
print("\n")

print("Open file (with) keyword: ")
with open("exp1.txt") as file:  
    data = file.read() 
print(data)

f=open('file1','w')
f.write("Dr.D.Y. Patil College of Engineering & Technology")
'''f1=open('file1','r')
print(f1.read())'''