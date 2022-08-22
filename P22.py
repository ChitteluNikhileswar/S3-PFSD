class Student:
    def __init__(self,id,name,cgpa):
        self.id=id
        self.name=name
        self.cgpa=cgpa
s=Student(10,"ABC",9.5)
setattr(s,cgpa,9)
print(getattr(s,"name"))
delattr(s,"name")
print(getattr(s,"name"))
delattr(s,"id")
print(getattr(s,"id"))