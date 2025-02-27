class circle :
    def __init__(self,radius):
     self.radius= radius

    def display_area(self)  :
     self.area = 3.14 * self.radius * self.radius
     print("area:",self.area)

A1= circle(10) 
A2= circle(7)
print(A1.display_area())    

