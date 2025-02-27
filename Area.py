class rectangle:
    def __init__(self,height,breadth):
     self.height = height
     self.breadth = breadth

    def display_area(self):
     self.area=(self.height)*(self.breadth)
     print("area:",self.area)

A1=rectangle(10,2)
A2=rectangle(12,5)

print(A2.display_area())

