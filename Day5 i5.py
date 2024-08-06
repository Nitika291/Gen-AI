"""Create a base class Person with attributes like name and age. Define a method introduce that prints a generic introduction. Create a subclass Student inheriting from Person. Add an attribute school to Student. Override the introduce method in Student to use super() to call the base class method and then add details about the school."""
# Base class Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# Subclass Student inheriting from Person
class Student(Person):
    def __init__(self, name, age, school):
        super().__init__(name, age)
        self.school = school

    def introduce(self):
        super().introduce()
        print(f"I am a student at {self.school}.")


# Example usage
if __name__ == "__main__":
    person = Person("Nitika", 23)
    person.introduce()

    student = Student("Nitika", 23, "MAHARSHI DAYANAND UNIVERSITY")
    student.introduce()
