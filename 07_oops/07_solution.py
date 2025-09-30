
#Static Method
#Add a static method to Car class that returns a general description od cars


class Car:
    total_cars =0


    def __init__(self, brand ,model):
        self.__brand = brand
        self. model= model
        self.total_cars  = Car.total_cars +1


    def full_name(self):
        return f"{self.__brand} {self.model}"   

    def get_brand(self):
        return self.__brand
    

    def fuel_type(self):
        return "Petrol, Diesel"
    
    @staticmethod
    def general_description():
         return "Cars are a mode of transport"
    
class Electric_Car(Car):
        def  __init__(self,brand, model, battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size

        def fuel_type(self):
                return "Electric"
            


my_car= Electric_Car("Toyota", "Camry",75)
Car("Tata","Nexon")

# print(my_car.general_description())
print(Car.general_description())
# print(my_car.fuel_type())
  #  print(my_car.total_cars)
  #  print(my_car.full_name())


       