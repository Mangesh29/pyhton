#Find the First Non-Repeated Character

input_str = input("Enter a string:")
char_count ={}

for char in input_str:
    print(char)
"""char in char_count:
        char_count[char] += 1
    else:
        char_count[char] =1

print("char count:", char)"""


if input_str.count(char) ==1:
    print("First non-repeated character is:",char)
     
else:
    print("All characters are repeated:")
    