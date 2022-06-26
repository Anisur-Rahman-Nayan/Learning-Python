class triangle:
	def __init__(self,base,height):
		self.base=base
		self.height=height
	def calcuarea(self):
		r=self.base*self.height*0.5
		print('area of triangle is',r)
t1=triangle(10,20)
t1.calcuarea()
t2=triangle(20,30)
t2.calcuarea()