
 # Function with **kwargs
# create a function that any number of keyword arguments and prints them in the format 

#key: value


def print_kwagrs(**kwargs):
    for key,values in kwargs.items():
        print(f"{key}: {values}")

    

 


print_kwagrs(name ="shatiman", power="lazer")
print_kwagrs(name ="shatiman")
print_kwagrs(name ="shatiman", power="lazer" , enemy ="dr.Jackaal")