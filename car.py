#creating a class
class Cars:
    model="Subaru"
    make="Toyota"
    color="Black"
    registration="124KBK"

#creating an instance of a class
class Car:
    def __init__(self, model, make, color, registration):
        self.model=model
        self.make=make
        self.color=color
        self.registration=registration
       

