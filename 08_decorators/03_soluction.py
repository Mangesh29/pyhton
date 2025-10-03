 
import time

def cache(func):
    cache_value={}
    print(cache_value)

    def wrapper(*args):
        if args in cache_value:
           print("Fetching from cache")
        return cache_value[args]
        result =func(*args)
        cache_value[args]=result
        return result
    return wrapper
 
@cache
def  long_running_function(a,b):
    time.sleep(4)
    return a+b



print(long_running_function(2,3) )  # This will take approximately 4 seconds to execute
print(long_running_function(2,3))   # This will be instantaneous on subsequent calls