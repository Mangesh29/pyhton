
# Timing Function Execution
#Write a decorators that measures the time a function takes to exeute

import time

def timer (func):
    def wrapper(*args, **kwargs):
        start =time.time()
        result= func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper


@timer
def example_function(n):
    time.sleep(n)
 

example_function(2)  # This will take approximately 2 seconds to execute