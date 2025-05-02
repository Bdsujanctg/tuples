class Person:
    def __init__(self,name,idnumber):
        self.idnumber=idnumber
        self.name=name
    def display(self):
        print(self.name)
        print(self.idnumber)
class employee(Person):
    def __init__(self,name,idnumber,salary,post):
        self.salary=salary
        self.post=post
        
        Person.__init__(self,name, idnumber)
    def display2(self):
        print(self.salary)
        print(self.post)
obj=employee("Rahul",230485,30000,"intern")
obj.display() 
obj.display2()
