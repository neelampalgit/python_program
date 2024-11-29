# *****************Control Flow Statement **************************
# 1. **********Conditional stmt *******************
# if condition:
#   do this
# else:
#   do this

# print("******* WELCOME TO THE ROLLERCOASTER *********")
# height= int(input("What is your height in cms?"))
# print(type(height))
#
# if height>=120:
#     print("Congrats, You can ride rollercaoster!")
# else:
#     print("Sorry, You can need to grow taller before you ride rollercaoster!")

# Conditions - comparsion operators
# >
# <
# >=
# <=
# ==
# !=

#************ Exercise - Check whether nbr is odd or even
# number= int(input("***********Enter the number to check of odd/even test:"))
# if number%2 == 0:
#     print(f"{number} is even")
# else:
#     print(f"{number} is odd")

#*************** Nested If-else statements ***********************
# Nested If statement:
# if condition:
#       if another condition:
#           do this
#       else:
#           do this
# else:
#      do this
# ****** Python implementation
# if condition1:
#     do this
# elif condition2:
#      do this
# elif condition3:
#      do this
# else:
#      do this

# print("******* WELCOME TO THE ROLLERCOASTER *********")
# height= int(input("What is your height in cms?"))
#
# if height>=120:
#     print("Congrats, You can ride rollercaoster!")
#     age = int(input("What is your age?"))
#     if age < 12:
#         print("Ticket Charges: $5")
#     elif age <=18:
#         print("Ticket Charges: $7")
#     else:
#         print("Ticket Charges: $12")
# else:
#     print("Sorry, You can need to grow taller before you ride rollercaoster!")

# *******************************
# ********************************* Exercise  **************************************************************************
# Write a program that works out whether if a given year is a leap year.
# A normal year has 365 days, leap year have 366 with an extra day in february.
# This is how you work out whether if a particular year is a leap year
#     on every year that is divisible by 4 with no remainder
#     except every year that is evenly divisible by 100 with no remainder
#     unless the year is also divisible by 400 with no remainder
# *********************************************************************************************************************
# ********************************* Exercise  **************************************************************************
# Build an automatic pizza order program.
# Based on user's order, work out their final bill.
# Small pizza($)(S) : $15
# Medium pizza($)(M) : $20
# Large pizza($)(L) : $25
# Add pepperoni for Small pizza($) (Y or N) : $2
# Add pepperoni for medium or large pizza(Y or N) : $3
# Add extra cheese for any size (Y or N) pizza($) : $1
# *********************************************************************************************************************
# print("Thank you for choosing Python Pizza Deliveries!")
# size = input("What size pizza do you want? S, M or L")
# add_pepperoni = input("Do you want pepperoni? Y or N")
# extra_cheese = input("Do you want extra cheese? Y or N")

# ******************************* LOVE CALCULATORS **********************************************************************
# Write a program that tests the compatiability between two people
# To work out the love score between two people:
#   1. Take both people's name and check for the number of times the letters in the word TRUE occurs.
#   2. Then check for the number of times the letters in the word LOVE occurs.
#   3. Then combine these numbers to make a 2 digit number.
# For Love scores less than 10 or greater than 90, the message should be:
# "Your score less than 10 or greater than 90, then message should be:
# "Your score is 'x' you go together like coke and mentos
# For love scores between 40 and 50, the message should be:
# "Your score is 'x' you are alright together.
# otherwise, the message will just be their score. e.g: "Your score is z"
# *********************************************************************************************************************

print("The Love calculator is calculating your score...")
name1 = input("What is your name?") #neelam
print(name1.count("e"))
name2 = input("What is their name?") #aarshi
# comined_name = name1+name2 #neelamaarshi
# t=comined_name.count("t") #t=0
# r=comined_name.count("r") #t=1
# u=comined_name.count("u") #t=0
# e=comined_name.count("e") #t=2
# true=t+r+u+e #3
#
# l=comined_name.count("l") #t=1
# o=comined_name.count("o") #t=0
# v=comined_name.count("v") #t=0
# e=comined_name.count("e") #t=2
# love=l+o+v+e #3
#
# score = 33
