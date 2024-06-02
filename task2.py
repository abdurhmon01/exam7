class Circle:
    PI=3.14
    def __init__(self,R):
        self.R=R
    def get_area(self):
        return 2 * self.PI * self.R**2
    def get_diametr(self):
        return 2 * self.R
    def get_circumference(self):
        return 2 * self.PI * self.R
    def get_radius(self):
        return self.R
circle=Circle(R=5)
print(circle.get_area())
print(circle.get_diametr())
print(circle.get_circumference())
print(circle.get_radius())