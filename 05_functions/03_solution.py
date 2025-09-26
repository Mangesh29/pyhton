##Polymorphism in Functions
#Write a function multiply that multiplies two numbers, but can also accept and multiply string


def multiply(a,b):
    return a*b

print(multiply(5,6))
print(multiply('Hello',5)) 
print(multiply(3,'chai'))


#Polymorphism in Python means “many forms”: the same operation (or interface) works with different types/objects.
# same function name but different  type of parameters.