#Program of Hybrid inheritance in Python
class Company:

    def func1(self):
        print ('This function is in Company.')

class Emp1(Company):

    def func2(self):
        print ('This function is in Employee 1.')

class Emp2:

    def func3(self):
        print ('This function is in Employee 2.')

class Emp3(Emp1, Emp2):

    def func4(self):
        print ('This function is in Employee 3.')


object = Emp3()
object.func1()
object.func2()
object.func3()
object.func4()