class cal5:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def calarea(self):
        self.ans = self.length * self.breadth

    def display(self):
        print("area of rectangle : ",self.ans)

c=cal5(6,7)
c.calarea()
c.display()
