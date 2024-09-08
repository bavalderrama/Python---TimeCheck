################################################################
# Script Name: TimeCheck.py
# Title: Time Check
# Description: Leveraging sorting algorithm to ensure speed test meets network requirements
# Network requirement: small and large tests should take under 100ms
# Author: Bernardo Valderrama
# Date: Apr 7th, 2024
################################################################

import random

def generate_random_list(n):
    # First, generate random list 'result' with values 1 thru n
    result = []
    for k in range(0,n):
      result.append(k+1)
    # Then, swap the values in 'result' starting with 'last value -1'
    # all the way down to result[1], in decrementing steps of -1
    # - No need to change result[0] -
    # we do this while generating random index numbers between 0 and n-1 for the random swap
    for i in range(n-1,1,-1):
      j = random.randint(0,n-1)
      result[i],result[j] = result[j],result[i]
    return result

#importing time library
import time

# SMALL TEST
start = time.time()
generate_random_list(100) #using generate_random_list function defined above with 100 numbers
test_time = (time.time() - start) * 1000
print(f'Small test took {test_time:.1f} ms')
#assert test_time < 100, 'Too slow!'

# LARGE TEST
start = time.time()
generate_random_list(10000) #using generate_random_list function defined above with 10000 numbers
test_time = (time.time() - start) * 1000
print(f'Large test took {test_time:.1f} ms')
#assert test_time < 100, 'Too slow!'