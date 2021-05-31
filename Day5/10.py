class parentclass():

    def func1(self):
        print("parent method called")

class childclass(parentclass):

    def func1(self):
        print("child method called")

c = childclass()
c.func1()

p = parentclass()
p.func1()
