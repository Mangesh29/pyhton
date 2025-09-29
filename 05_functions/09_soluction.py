# Generator Function with yield#
#Write a generator function that yields even numbers up to a specified limit


def even_numbers(limit):

    
    for i in range(2, limit + 1, 2):
      yield i



 # Example usage:  
for num in even_numbers(10):
         print(num)
         # Output: 2, 4, 6, 8, 10
