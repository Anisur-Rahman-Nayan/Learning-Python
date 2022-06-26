class Student:
    name = ""
    roll = ""
    gpa = ""

student1 = Student()
# print(isinstance(rahim,Student))

student1.name = "AR NAYAN"
student1.roll = 24
student1.gpa = 3.5

student2 = Student()
student2.name = "Leo Messi"
student2.roll = 21
student2.gpa = 4

print(f"Name : {student2.name}, \n Roll : {student2.roll}, \n GPA : {student2.gpa}")