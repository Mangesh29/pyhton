 


class Car:
    total_car =0  #class variable to keep track of total cars

    def __init__(self, brand,model):
        self.__brand =brand
        self.model=model
        Car.total_car +=1  #increment total cars when a new car is created

    def full_name(self):
            return f"{self.__brand} {self.model}"
        
    def get_brand(self):
            return self.__init__ +"!"
        
    def fuel_type(self):
     
            return "Petol or Diesel"
        
class ElectricCar(Car):
        def __init__(self,brand,model,battery_size):
            super().__init__(brand, model)
            self.battery_size=battery_size

        def fuel_type(self):
 
            return "Electricity"


 
   #my_tasala =ElectricCar("Tasala", "Model s",100)
   #print(my_tasala.fuel_type())

Car("Tata","Safari")
 

Car("Tata","Safari")
 

print(Car.total_car) #accessing class variable to get total number of cars created



