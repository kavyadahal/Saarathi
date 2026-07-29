class Student:
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def average(self):
        total = 0
        for sub in self.scores:
            total += sub
        return total / len(self.scores)

    def grade(self):
        average = self.average()

        if average >= 80:
            return "A"
        elif average >= 60:
            return "B"
        elif average >= 40:
            return "C"
        else:
            return "Needs work"

    def report(self):
        print(f"Name: {self.name}")
        print(f"Average: {self.average():.1f}")
        print(f"Grade: {self.grade()}")

s1 = Student("Kavya", [80, 90, 70])
s1.report()

s2 = Student("Prachi", [20, 10, 30])
s2.report()