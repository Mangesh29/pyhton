

# Property Decorators
#Use a property decorator in the Car class to make the model attribute read-only


class Car:
    total_cars =0


    def __init__(self, brand ,model):
        self.__brand = brand
        self. __model= model
        self.total_cars  = Car.total_cars +1


    def full_name(self):
        return f"{self.__brand} {self.__model}"   

    def get_brand(self):
        return self.__brand
    

    def fuel_type(self):
        return "Petrol, Diesel"
    
    @staticmethod
    def general_description():
         return "Cars are a mode of transport"
    
    @property
    def  model(self):
         return self.__model
         

    
class Electric_Car(Car):
        def  __init__(self,brand, model, battery_size):
            super().__init__(brand,model)
            self.battery_size = battery_size

        def fuel_type(self):
                return "Electric"
            


my_car= Car("Toyota", "Camry")
#my_car.model ="City"
Car("Tata","Nexon")

 
print( my_car.model)
 


       