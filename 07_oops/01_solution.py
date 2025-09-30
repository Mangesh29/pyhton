#Basic Class and Object
#Create a Car class with attributes like brand and model. Then create an instance of this class




class Car:
   def __init__(self, brand, model):   # self refer to the instance of the class
                                       # self is used to access variables that belonges to the class 
        self.brand =brand
        self.model = model               # constructor to initialize attributes




my_car = Car("Toyota", "Corolla")         # calling the class to create  an object
print(my_car.brand)                # accessing the attributes of the class using the object
print(my_car.model)                     # accessing the attributes of the class using the object

my_new_car =Car("Tata", "Nexon")           #  creating another object of the class
print(my_new_car.brand)
print(my_new_car.model)


#output:Toyota,Corolla,Tata,Nexon