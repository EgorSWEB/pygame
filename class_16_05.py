class Student:
    name = "def"

    def __init__(self, n, age):
        self.name = n
        self.age = age

    def hello(self):
        print(self.name, ", мне", self.age)

st1 = Student("Алексей", 10)

st2 = Student("Владимир", 41)

st1.hello()
