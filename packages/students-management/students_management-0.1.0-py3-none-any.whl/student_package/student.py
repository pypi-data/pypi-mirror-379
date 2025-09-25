class Student:
    def __init__(self, id, name, age, grades):
        self.id = id
        self.name = name
        self.age = age
        self.grades = grades
    
    def add_grade(self, mark):
        if mark<=100 and mark>0:
            self.grades.append(mark)
            return True
        else:
            return False

    def average_grade(self):
        total = 0 
        for i in self.grades:
            total += i
        return total/len(self.grades)
    
    def __str__(self):
        return f"Student name: {self.name}, ID: {self.id}, Grades: {self.grades}, Age: {self.age}"