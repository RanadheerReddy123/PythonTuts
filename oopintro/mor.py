class Parent:
    def Bike(self):
        print('I have a Bike')
class Child(Parent):
    def Bike(self):
        print('I have a Car')
obj = Parent()
#obj = Child()
obj.Bike()