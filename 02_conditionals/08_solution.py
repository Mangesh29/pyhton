 
Password ="Secure3p@ss"
Password_length = len(Password)

if Password_length <6:
    strength ="Weak"

elif Password_length <=10:
    strength ="medium"

else:
    strength ="Strong"



print("Password strength is :", strength)    