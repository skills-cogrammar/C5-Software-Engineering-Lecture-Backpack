class Student:

    def __init__(self, fullname):
        self.fullname = fullname
        self.subjects = []
        self.grades = []

    def get_final_grade(self) -> float:
        return sum(self.grades)/len(self.grades)
    

class EngineeringStudent(Student):

    def __init__(self, fullname):
        super().__init__(fullname)
        self.final_exam = 0

    def get_final_grade(self):
        return (super().get_final_grade()/2) + (self.final_exam/2)
    

class LawStudent(Student):

    def __init__(self, fullname):
        super().__init__(fullname)
        self.final1 = 0
        self.final2 = 0

    def get_final_grade(self):
        return (super().get_final_grade()/100*30) + ((self.final1+self.final2)/200 * 70)
    

def print_scores(students):
    for student in students:
        print(f"{type(student)} {student.get_final_grade()}")



students = []
temp_student = Student("John")
temp_student.grades = [70, 68, 75]
students.append(temp_student)

temp_student = LawStudent("Tina")
temp_student.grades = [70, 68, 75]
temp_student.final1 = 65
temp_student.final2 = 72
students.append(temp_student)

temp_student = EngineeringStudent("Michelle")
temp_student.grades = [70, 68, 75]
temp_student.final_exam = 68
students.append(temp_student)

print_scores(students)
print("-"*80)
students.sort(key = lambda x : x.get_final_grade())
print_scores(students)