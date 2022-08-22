class Reservation:
    a=int(input("Enter your name"))
    b=int(input("Enter your national id"))
    c=int(input("Enter your class"))
    def Tickets(self,f,s,t):
        for f in 10:
            if f>10:
                print("Ticket sucessfully reserved")
            else:
                print("Tickets are full")
        for s in 10:
            if s>20:
                print("Ticket sucessfully reserved")
            else:
                print("Tickets are full")
        for t in 10:
            if t>10:
                print("Ticket sucessfully reserved")
            else:
                print("Tickets are full")
class Child(Reservation):
    def available(self,f,s,t):

a=Child()
a.Tickets()
a.available()





