 # Function with *args
# Write a function that takes variable number of arguments and returns their sum

 

def sum_numbers(*args):
    print(args)  # args as tuple
    for i in args:
        print(i *2)
    return sum(args)

print(sum_numbers(1,2,3,))    # argummnt  as tuple
print(sum_numbers(10,20,30,40))
 
