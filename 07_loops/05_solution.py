#Polymorphis
#Demonstrate polymorphism by defining a method fuel _type in both Car and ElectricCar Classes,but with different behaviors


# Polymorphism  is  the ability to present the same interface for differing underlying data types.
class Car:
    def __init__(self, brand,model):
        self.__brand =brand
        self.model=model

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


 
my_tasala =ElectricCar("Tasala", "Model s",100)
print(my_tasala.fuel_type())


safari =Car("Tata","Safari")
print(safari.fuel_type())



