


import math

def circle_stats(radius):                
     
     # area of cricle
     # area = πr².
     # circumference of circle     
        # circumference = 2πr

         area =math.pi *radius **2

         circumference = 2* math.pi *radius
         return area, circumference

a,c =(circle_stats(5))  

print(f"Area: ", a, "circumference:") 
