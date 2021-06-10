class publisher():

    def __init__(self,title):
        print("title : ",title)

class book(publisher):

    def __init__(self,page_no):
        print("Page_no : ",page_no)

class tape(publisher):

    def __init__(self,time):
        print("Time for Playing : ",time)

c1=publisher("Jeel")
c2=book("80")
c3=tape("3hrs")