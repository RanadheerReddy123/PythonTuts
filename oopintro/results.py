class Student:
    school = 'TCW'
    def __init__(self):
        self.marks1 = 'Marks1'
        self.marks2 = 'Marks2'
        self.marks3 = 'Marks3'
    #Instance Methods
    #=== GET Methods === Accessors
    def get_m1(self):
        return self.marks1


    def get_m2(self):
        return self.marks2


    def get_m3(self):
        return self.marks3


    #=== Set Methods === Mutators
    def set_m1(self, value):
        self.marks1 = value


    def set_m2(self, value):
        self.marks2 = value


    def set_m3(self, value):
        self.marks3 = value


     #Class methods
    @classmethod
    def get_school(cls):
        return cls.school

    #Static methods
    @staticmethod
    def sayhello():
        print("Hello Student")


s1 = Student()
s2 = Student()

print('School Name:', Student.get_school())
Student.sayhello()

s1.set_m1(79)
print(s1.get_m1())

s2.set_m1(96)
print(s2.get_m1())


