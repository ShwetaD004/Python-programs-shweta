#Program of hierarchical inheritance
class A:
    def function1(self):
        print("Parent class A")

class B(A):
    def function2(self):
        print("Child class 1")

class C(A):
    def function3(self):
        print("Child class 2")

obj1=B()
obj1.function1()
obj1.function2()
obj2=C()
obj2.function3()