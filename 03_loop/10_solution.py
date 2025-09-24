 # Exponential Backoff
# Implement on exponetial backoff strategy the doubles the wait time between retries, statting from 1 second, but stopes after 5 retries

import time

wait_time = 1  # initial wait time in seconds
max_retries = 5
attempts =0

while attempts < max_retries:
    print("Attempt", attempts+1,"-wait time",wait_time,)
    time.sleep(wait_time)  # Simulate wait time
    wait_time *= 2  # Double the wait time
    attempts +=1
    