
# Scope is block od code where a vriable  is accessible in a program  
# Local scope : v ariable defined inside a function is in local scope 
#Globlal scope : variabe defined outside a function is in global scrope 


username ="chaiaurcode"        #global scope

def func():
   username="codewit pyhton"      # local scope
   print(username)


print(username)
func()



# x=99
'''
def func2(y):
   z=x+y
   return z


result=func2(1)
print(result)




def func3():
    global x
    x=12
    

 

print(x)



'''

def chaicoder(num):
   def actual(x):
      return x* num
   return actual

def chaicoder(num):
   def actual(x):
      return x** num
   return actual

f = chaicoder(2)
g= chaicoder (3)

print(f(3))
print(g(3))


