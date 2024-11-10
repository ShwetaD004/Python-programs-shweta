class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunction(self):
        print("Hello, my name is ",self.name)
        print("& my age is ",self.age)
p1=person("Shweta",20)
p1.myfunction()