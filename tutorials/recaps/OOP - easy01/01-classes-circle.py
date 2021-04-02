class Circle():
    pi = 3.14
    def __init__ (self, radius=1):
        self.radius = radius
    
    def get_circumference(self):
        return self.radius * self.pi * 2

my_circle = Circle(30) ## this overrides the default value of radius (__init__)
print("Pi is: "+str(my_circle.pi)+". Circumference is: "+str(my_circle.get_circumference()))
