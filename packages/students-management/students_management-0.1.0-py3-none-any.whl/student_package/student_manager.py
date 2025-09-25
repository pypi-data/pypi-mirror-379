# import student

class StudentManager:
    def __init__(self, students = []):
        self.students = students

    def add_student(self, student):
        self.students.append(student)
        return True
    
    def remove_student(self, id):
        for i in self.students:
            if i.id == id:
                self.students.remove(i)
                return True
        return False
    
    def all_students(self):
        return self.students
    
    def get_student(self, id):
        for i in self.students:
            if i.id == id:
                return i