#this is a comment#

class myclass:
    name = ""
    def func1(self):
        print("Hello function1")

    def func2(self, name):
        self.name=name

    def func3(self):
        print("Value is : ", self.name)

m1 = myclass()
m1.func1()
m1.func2("Akash technolabs")
m1.func3()
