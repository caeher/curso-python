class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello!, I am a person.")


class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")


student1 = Student("John", 20, 12345)
student1.greet()


class LivingBeing:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

class Persona(LivingBeing):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        super().greet()
        print(f"Hello, my age is {self.age}")

class Estudiante(Persona):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def greet(self):
        super().greet()
        print(f"Hello, my student ID is {self.student_id}")

estudiante1 = Estudiante("John", 20, 12345)
estudiante1.greet()