 # Encapsulation
#Modify the Car class to encapsulate the brand attribute,making it private, and provide a getter method for it .


class Car:
    def __init__(self, brand, model):    #class Car
        self.__brand = brand            #private attribute
        self.model=model          #public attribute

    def full_name(self):  #method
        return f"{self.__brand} {self.model}" 
    
    def get_brand(self):    #getter method
        return self.__brand + "!"
    
    

class ElectricCar(Car):     #class ElectricCar that inherits from 
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)  
        self.battery_size=battery_size


my_tasala=ElectricCar("Tasala","Model s",100)
 

print(my_tasala.get_brand())   