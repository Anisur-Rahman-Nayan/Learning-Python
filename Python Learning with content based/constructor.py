class Students:
    name=""
    roll=""
    gpa=""

    def __init__(self ,name , roll , gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, \n Roll: {self.roll}, \n GPA: {self.gpa}")

student1 = Students("AR NAYAN",24,3.5)
student1.display()

student2 = Students("Leo Messi",21,4)
student2.display()