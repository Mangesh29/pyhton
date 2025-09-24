# Prime Number Checker
#Check if a Number is prime

num =int(input("Enter your number:"))

num_is_prime=True

if num>1:
    for i in range(2,num):
        if num%i==0:
            num_is_prime=False
         
            break
    


print("number is prime:",num_is_prime)
