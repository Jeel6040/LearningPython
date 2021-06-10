class arith():

    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
        print("Value of n1 is :",n1)
        print("Value of n2 is :",n2)
        add = n1 + n2
        print("Addition :",add)
        sub = n1 - n2
        print("Subtraction :",sub)
        multiply = n1 * n2
        print("Multiplication :",multiply)

a1 = arith(10,20)