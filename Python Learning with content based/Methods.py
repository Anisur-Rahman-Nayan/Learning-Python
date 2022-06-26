class Students :
    name = ""
    roll = ""
    gpa = ""

    def set_value(self,name,roll,gpa):
        self.name = name
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Name: {self.name}, \n Roll: {self.roll}, \n GPA: {self.gpa}")

student1 = Students()
student1.set_value("Nayan",24,3.5)
student1.display()

student2 = Students()
student2.set_value("Leo Messi",21,4)
student2.display()