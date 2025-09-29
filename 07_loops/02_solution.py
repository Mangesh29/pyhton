#Class Method and Self
# Add a method to the Car class that displays the full name of the car (brand, and model)


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model


    def  full_name(self):
        return f"{self.brand} {self.model}"  # method to display full name of the car
    


my_car =Car("Toyoto", "Innova")
print(my_car.brand)       # calling the method using the class name and
print(my_car.model)
print(my_car.full_name())     # calling the method using the instance of the class
