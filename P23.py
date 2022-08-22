class Base:
    class block
class Dervied1(Base):
    class block
class Dervied2(Base):
    class block
class DC(Dervied1,Dervied 2)
    class block

Note:Object has to be created only to derived class.
Ex:Single inhertiance
class Parent:
    def fn1(self):
        print("this is parent class")
class Child(Parent):
    def fn2(self):
        print("this is child class")
ob=Child( )
ob.fn2( )
ob.fn1( )
