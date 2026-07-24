"""class Person:
    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)


class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)   # Calls Person's constructor
        self.score = score

    def display(self):
        super().display()         # Calls Person's display()
        print("Score:", self.score)


# Create object
student1 = Student("Kavya", 95)

# Access inherited and child methods
student1.display()"""

class Person:
    def __init__(self, name):
        self.name = name
        self.name_k_h0 = name

class Student(Person):
    def __init__(self, name, score):
        super().__init__(name)
        self.score = score

s = Student("Ram",78)
print(s.name_k_h0)