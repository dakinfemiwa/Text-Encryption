#IMPORTS
#Imports random
import random
#Imports math
import math

#BLANK VARIABLES
#The variable which will have the 8 character key
ascII_value = ""
#This is for the sum of the numbers randomly chosen
numbers = 0

def ascII_converter():
  global numbers, ascII_value
  for digit in range(0, 8):
    rand = random.randint(33, 126)
    numbers = numbers + rand
    character = chr(rand)
    ascII_value += character
  return ascII_value

def off_set_value_calculator():
  global numbers, off_set_value
  for digit in range(0, 8):
    numbers += ord(ascII_value[digit])
  average = (numbers / 8)
  average = math.floor(average)
  off_set_value = average - 32
  return off_set_value
  
#Perform functions  
ascII_converter();
off_set_value_calculator();

#Displays the 8 cahracter code
print("Your 8 character key is: \n\t{}".format(ascII_value))

