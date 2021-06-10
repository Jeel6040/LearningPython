class cal3:
    def __init__(self,p,r,t):
        self.n1 = p
        self.n2 = r
        self.n3 = t

    def calinterest(self):
        self.interest = ((self.n1*self.n2*self.n3)/100)

    def display(self):
        print("Interest of given value is ",self.interest)

c=cal3(1000,1,2)
c.calinterest()
c.display()