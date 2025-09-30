 #Inheritance
#Create an Electric class that inherits from the Car class and has an additional attribute battery_size



class Car():    #class Car
    def __init__(self, brand, model):
        self.brand = brand
        self.model =model

    def full_name(self):
            return f"{self.brand} {self.model}"
        
class Electric_car(Car):         #class Electric that inherits from Car
        def __init__(self, brand, model,battery_size):   #additional attribute battery_size
            super().__init__(brand, model)  #call the parent class constructor
            self.battery_size= battery_size     #initialize the additional attribute
          


my_tasla = Electric_car("Tesla","model","100KWh")
print(my_tasla.brand)

print(my_tasla.full_name())
