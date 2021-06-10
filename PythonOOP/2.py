class cal2:
    def setdata(self, r):
        self._rad = r

    def area(self):
        self._total_area = 3.14*self._rad*self._rad

    def display(self):
        print("area of circle is ",self._total_area)

c = cal2()
c.setdata(12)
c.area()
c.display()