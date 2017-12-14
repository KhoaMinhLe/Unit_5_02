# Created by: Khoa Le
# Created on November 2017
# Created for ICS3U
# This program finds the largest number in an array of random numbers.

from numpy import random

def max_array(array = []):
    max_value = array[0]
    
    for single_value in array:
        if max_value < single_value:
            max_value = single_value
    return max_value

counter = 0
random_values = []
while counter < 10:
    single_value = random.randint(1, 10 + 1)
    print(single_value)
    random_values.append(single_value)
    counter = counter + 1

highest_number = max_array(random_values)
print("The largest number is ") + str(highest_number)
