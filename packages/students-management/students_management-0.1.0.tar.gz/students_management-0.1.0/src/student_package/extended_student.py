from . import student


class PhD (student.Student):
    def __init__(self, lab, id, name, age, grades):
        super().__init__(id, name, age, grades)
        self.lab = lab

    def __str__(self):
        return super().__str__() + f", Lab: {self.lab}"

class Master (student.Student):
    def __init__(self, thesis, id, name, age, grades):
        super().__init__(id, name, age, grades)
        self.thesis = thesis

    def __str__(self):
        return super().__str__() + f", Thesis: {self.thesis}"


class Undergraduate(student.Student):
    def __init__(self, clubs, id, name, age, grades):
        super().__init__(id, name, age, grades)
        self.clubs = clubs
    
    def __str__(self):
        return super().__str__() + f", Clubs: {self.clubs}"