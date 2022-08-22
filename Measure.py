import math


class Calculations:
    def Rectangle(self,a,b):
        print("Area of rectangle:",a*b)
        print("Perimeter of rectangle:",2*(a+b))
    def Triangle(self,l,b,h):
        print("Area of triangle:",1/2*h*b)
        print("Perimeter of triangle:",l+b+h)
    def Circle(self,r):
        print("Area of circle:",math.pi*r*r)
        print("Perimeter of circle:",2*math.pi*r)

a=Calculations()
a.Rectangle(6,4)
a.Triangle(2,4,6)
a.Circle(4)



