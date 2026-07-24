class Student:
    ##Constructor:
    def __init__(self, name:str, score:int):
        self.name = name
        self.score = score

    def grade(self) -> str:
        if self.score >= 80: return "A"
        return "B"

print(Student("Kavya", 78).grade())
s = Student("Kavya",78)
print(s.name)

