#IMPORTS
#Imports random
import random
#Imports math
import math

#BLANK VARIABLES
#The variable which will have the 8 character key
eight_digit_character = ""
#This is for the sum of the numbers randomly chosen
numbers = 0

#This is the function which converts the randomly selected numbers into ASCII code
def ascII_converter():
  #Makes the eight_digit_character variable acceessible on all functions and outside subprograms
  global eight_digit_character
  #A loop which selects a number from 33 to 126 randomly and coverts it to its ASCII character, and then generates the ASCII values into an 8 digit character
  for digit in range(0, 8):
    #Randomly selects a number from 33 to 126 randomly
    rand = random.randint(33, 126)
    #Converts the number into its ASCII character
    character = chr(rand)
    #Adds the ASCII character onto the
    eight_digit_character += character
  #Returns the eight_digit character
  return eight_digit_character

#This function calculates the offset factor of the 8 digit character
def off_set_value_calculator():
  #Makes the offset factor variable and the blank numbers variable set on line 11 accessible in all functions and outside subprograms
  global off_set_value, numbers
  #A loop which converts every digit of the 8 digit character back into decimal and finds the sum of all the values
  for digit in range(0, 8):
    #Converts every digit of the character key and converts it into a decimal and finds the sum of each value
    numbers += ord(eight_digit_character[digit])
  #Finds the average of the sum derived in line 35. As the sum of integers divides by 8 the average will never be a recurring decimal
  average = (numbers / 8)
  #Rounds the average down to the nearest whole number
  average = math.floor(average)
  #Subtracts the rounded average by 32 to find the off-set value
  off_set_value = average - 32
  #Returns the offset value
  return off_set_value
  
#Perform functions  
ascII_converter();
off_set_value_calculator();

#Displays the 8 cahracter code
print("Your 8 character key is: \n\t{}".format(eight_digit_character))

