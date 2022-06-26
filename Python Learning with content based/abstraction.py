from abc import ABC,abstractmethod

class Shape(ABC):
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2
    @abstractmethod
    def calculation(self):
       pass

class Triangle(Shape):
    def calculation(self):
        result = self.dim1 * self.dim2 * 0.5
        print(f"area of Triangle : {result}")

class Rectangle(Shape):
    def calculation(self):
        result = self.dim1 * self.dim2
        print(f"area of Rectangle : {result}")



t1 = Triangle(10,20)
t1.calculation()
r1 = Rectangle(10,20)
r1.calculation()