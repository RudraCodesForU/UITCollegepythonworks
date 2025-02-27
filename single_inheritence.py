class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display_Person(self):
        print("My Name is {self.name}, and I am {self.age} years old." )   

class Teacher(Person):
     def __init__(self, name, age, department, experience, salary):
       self.name=name
       self.age=age
       self.department=department
       self.Experience=experience
       self.Salary=salary
T1=Teacher ( "RS",38,"Electrical",32,46000)
T2=Teacher ("SS",42,"Electrical",35,73000)
T3=Teacher ("RB",15,"IT",42,65000)         
print(T1) 


