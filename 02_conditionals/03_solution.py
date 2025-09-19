Mark=88

if Mark >= 101:
    print("Please verify your grade again")
    exit()
   

if Mark >=90:
    grade ="A"
elif Mark >=80:
    grade = "B"   
elif Mark >=70:
    grade = "C"
elif Mark >=60:
    grade = "D"        
else:
    grade = "f"

print("Grade",grade )