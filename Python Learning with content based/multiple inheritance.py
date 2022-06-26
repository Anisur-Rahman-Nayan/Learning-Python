class A:
    def display(self):
        print("I am inside A class !")

class B:
    def display(self):
        print("I am inside B class !")

class C(A,B):
    
        pass

ob1 = C()
ob1.display()