class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        return Student(m1, m2)
    def __gt__(self, other):
        s1tm = self.m1 + self.m2
        s2tm = other.m1 + other.m2
        if s1tm >s2tm:
            return True
        else:
            return False
s1 = Student(35, 65)
s2 = Student(75, 42)
s3 = s1 + s2
print(s3.m1, s3.m2)
print("S1TM:", s1.m1 + s1.m2)
print("S2TM:", s2.m1 + s2.m2)
if s1 > s2:
    print("s1 wins")
else:
    print("s2 wins")