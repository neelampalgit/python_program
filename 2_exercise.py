# name = input("What is your name?")
# print(name)
# length = len(name)
# print("Length is:", length)

#************************************************
# Exercise - There are 2 variables, a and b from input.
# # Write a program that switches the values stored in the variables a and b
# # a=10, b=20 => a=20,b=10
#
# a= input("Enter first number:")
# b= input("Enter second number:")
# print(f"B4 swapping, a is:{a}")
# print(f"B4 swapping, b is:{b}")
# temp= a
# a=b
# b=temp
# print(f"After swapping, a is:{a}")
# print(f"After swapping, b is:{b}")
#
# #********************************************
# a=100_000
# b=100_000
# print(a+b)

# ****************************************************************************************
#  PROJECT 1:   Food Fusion Name Generator
#  Create a program that generates the name of the dish by combining user's favorite food with  user's favorite fruit.
#  Requirements:
#
#  Display a welcome greeting for the program.
#  Prompt the user to input favorite food/cuisine.
#  Prompt the user to input favorite fruit.
#  Combine the both the names to generate favorite fusion dish
#  Display the generated fusion name to the user in some interesting statement.
# ********************************************************************************************************************
print("Welcome to the Food Fusion Name Generator")
food= input("Please enter your favorite food/cuisine: ")
fruit= input("Please enter your favorite fruit: ")
# foodFusion= food,fruit
print("The food fusion is",food+fruit)
print("The food fusion is",food,fruit)



