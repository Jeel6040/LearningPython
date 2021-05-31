class parent:

    def __init__(self):
        print("calling parent constructor")

    def parentmethod(self):
        print("Calling parentmethod")

class child(parent):
    def __init__(self):
        print("calling child constructor")

    def childmethod(self):
        print("calling childmethod")

c = child()
c.childmethod()
c.parentmethod()
