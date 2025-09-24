 #List Uniqueness Character
#Check if all elements in alist  are unique .if duplicate is found, exit the loop and print the duplicate
 
items =[ "apple","banana","orange","apple","mango"]

uniqe_item=set()

for item in items:
    if item in uniqe_item:
        print("Duplicate item found:",item)
        break
    uniqe_item.add(item)


print("All items are unique")