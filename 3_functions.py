
# def greet():
#     print("Hello Neelam!")
#
# # greet()
# # greet()
# # greet()
# # greet()
#
# def greet(name="ABC"):
#     print(f"Hello {name}!")
#
# greet("Neelam")
# greet("Falguni")
# greet("Prathima")
# greet("Bharath")
# greet()
#
# def greet(name, location):
#     print(f"Hello {name}, you are from {location}")
#
# greet("Neelam", "Pune")
# greet(location="Pune", name="Neelam")
#
# def add(num1,num2):
#     result = num1+num2
#     return result
#
# result = add(10,20)
# print(f"Sum is:", result)
#
# def add(num1,num2, num3):
#     result = num1+num2+num3
#     return result
#
# result = add(10,20,30)
# print(f"Sum is:", result)

#*args
def add(*args):
    result = sum(args)
    return result

# print("Sum of all nbrs is:",add(10, 20, 30, 40, 50, 100))

# Product of sum of numbers

def add(num1,num2):
    result = num1+num2
    # print(result)
    return result

res = add(5,5)
final_result = 20*res
print("final result:", final_result)


def greet(*name):
    print(f"Hello {name}!")
    for _ in name:
        print(f"Hello, {_}")

greet("Neelam","Falguni","Prathima","Bharath")

#*************************************
# Naming Conventions
# 1. snake_case
# 2. camelCase
# 3. PascalCase
# 4. kebab-case
# 5. Hungarian Notation - intRollNumber
# 6. URL, PI (all in UPPER SNAKE CASE)


#****************************  Exercise - Assignment *******************************
# Write a program that automatically prints the solution to the FizzBuzz game.
# These are the rules of the FizzBuzz game:
#   a. Your program should print each number from 1 to 100 in turn and include number 100
#   b. When the number is divisible by 3 then instead of printing the number it should print "Fizz"
#   c. When the number is divisible by 5, then instead of printing the number it should print "Buzz"
#   d. And if the number is divisible by both 3 and 5. eg. 15 then instead of the number it should print
#        "FizzBuzz"
# Output: 1,2,"Fizz",4,"Buzz","Fizz",7,8,"Fizz","Buzz",11,"Fizz",13,14,"FizzBuzz",...... 100
#*****************************************************************************************************

#****************************  Exercise - Assignment *******************************
# Password Generator
print("Welcome to the Password Generator!")
nr_letters = int(input("How many letters would you like in your password\n")) # 8
nr_symbols = int(input("How many symbols would you like in your password\n")) #1
nr_numbers = int(input("How many numbers would you like in your password\n")) #3
#abcd@123
letters = ['a','b','c','d','e','f','g','h','i','j','k', 'l', 'm','n','o','p','q','r','s','t',
           'u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
           'P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(', ')','*','+']




















