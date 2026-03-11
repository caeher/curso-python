class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hola, mi nombre es {self.name} y tengo {self.age}")


person1 = Person("Cristian", 22)
person2 = Person("Antonio", 25)

person1.greet()
