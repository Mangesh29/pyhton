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

   # print(isinstance(my_tasla,Car))   #check if my_tasla is an instance of Car   
    
   # print(isinstance(my_tasla,Electric_car))
 
class Battery:
      def battery_info(self):
            return "this is battery"

class Engine:
      def engine_info(self):
            return "this is engine"
      

class ElectricCar(Battery, Engine,Car):
      pass




my_new_tesla = ElectricCar("Tesla","Model S")
print(my_new_tesla.engine_info())
print(my_new_tesla.battery_info())

