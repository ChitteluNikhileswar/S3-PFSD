class Student:
    def.__init__(self,id,name):
        self.id=id
        self.name=name
    def display(self ):
        print(self.id,self.name)
s1=Student(10,"ABC")
s2=Student(20,"Def")
s1.display( )
s2.display( )