#1 Class Circle
# A Circle instance accepts attribute radius (r)
# It has a method area that returns the area (A) of the circle using the formula A=πr2
# It has a method to calculate circumference (c) using the formula C=2πr
class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        r = 3.142*(self.radius)*(self.radius)
        return f"the area of the circle is {r}"

    def circumference(self):
        c=2*(self.radius)*3.142
        return f"the circumference of the circle is {c}"   


#2 Class Square
# A Square instance accepts the attribute side (a)
# It has method area that returns the area (A) of the square using the formula A=a2
# It has a method to calculate the perimeter (P) of the square using the formula P=4a
   
class Square:
    def __init__(self, side):
        self.side=side
    def area(self):
        A=(self.side)*(self.side)
        return f"the area of the square is {A}"

    def perimeter(self):
        P=4*(self.side)
        return f"the perimeter of the circle is {P}" 

#3 Class Rectangle
# A Rectangle instance accepts two sides of a rectangle (w,l)
# It has method to calculate the area (A) of the rectangle using the formula A=wl
# It has a method to calculate the perimeter (P) 
# of the rectangle using the formula P=2(l+w)
class Rectangle:
    def __init__(self, width, length):
        self.width=width
        self.length=length
    def area(self):
        A=(self.width)*(self.length)
        return f"the area of the rectangle is {A}"

    def perimeter(self):
        P=2*(self.length+self.width)
        return f"the perimeter of the rectangle is {P}"

#4 Class Sphere
# A Sphere Instance accepts the radius of the sphere (r)
# It has a method to calculate the surface area (A) using the formula A=4πr2
# It has a method to calculate the volume (V) 
# of the sphere using the formula V = 4/3(πr3)
class Sphere:
    def __init__(self, radius):
        self.radius=radius
    def surface_area(self):
        A=4*(3.142)*(self.radius)*(self.radius)
        return f"the surface area of the sphere is {A}"

    def volume(self):
        V=4/3*(3.142)*(self.radius)*(self.radius)*(self.radius)
        return f"the volume of the sphere is {V}"
    

        
        

        
      
