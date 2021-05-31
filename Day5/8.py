class parent:
    def __init__(self):
        print("calling parent constructor")

    def parentmethod(self):
        print("calling parent method")

class child(parent):
    def __init__(self):
        print("calling child constructor")

    def childmethod(self):
        print("calling child method")

class child2(parent):
    def __init__(self):
        print("calling child2 constructor")

    def child2method(self):
        print("calling child2 method")

sc = child2()
sc.child2method()
sc.parentmethod()
