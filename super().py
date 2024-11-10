#Program of single inheritance using super()
class person:
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def printname(self):
        print(self.name,self.city)

class student(person):
    def __init__(self, name, city,age):
        super().__init__(name, city)
        self.age=age

    def show(self):
        print("Hello, I am a student. My name is ",self.name,".I am from ",self.city,".My age is ",self.age)

a=student("Shweta Davari","Kolhapur",20)
a.show()
a.printname()