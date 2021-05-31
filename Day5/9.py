class myparentclass1():

    def method_parent1(self):
        print("parent1 method called")

class myparentclass2():

    def method_parent2(self):
        print("parent2 method called")

class childclass(myparentclass1, myparentclass2):

    def child_method(self):
        print("child method")

class childclass2(myparentclass1, myparentclass2):

    def child_method2(self):
        print("child2 method")

c = childclass()
c.method_parent1()
c.method_parent2()
c.child_method()

c2 = childclass2()
c2.child_method2()
c2.method_parent1()
