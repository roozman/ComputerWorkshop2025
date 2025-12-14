class Person:
    def __init__(self, name):
        self.name = name
    def who_are_you(self):
        return self.name

class Student(Person):
    def __init__(self, name, student_id):
        # self.name = name
        super().__init__(name)
        self.id = student_id

    def who_are_you(self):
        return self.name, self.id 

x = Person("Rupert")

# print(x.who_are_you())

y = Student("Rupert", 123456)

y_name, y_id = y.who_are_you()
print(f"Name: {y_name}, Student ID: {y_id}")

