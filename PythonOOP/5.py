class employee:

    def __init__(selfself,name,designation):
        self.name=name
        self.designation=designation

class subclass(employee):

    def __init__(self,name,designation,salary):
        print("Name :", name,"\ndesignation :",designation,"\nsalary :",salary)

cf=subclass("Jeel","Webdeveloper","90000")