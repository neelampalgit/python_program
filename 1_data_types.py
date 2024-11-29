day = "Saturday"
print("Welcome to the class on:",day)
print("Welcome to the class on:"+day)
times=100
print("Welcome to the class:",times)
print("Good day!"*5)

# #******************************************************

# 1. Numeric data type - int, float, complex
a=10 #int
print("Data type of a is:", type(a))

a=10.3452343 #float
print("Data type of a is:", type(a))

a=10+2j #complex
print("Data type of a is:", type(a))

#2. String sata type
a="Do your homework"
print("Data type of a is:", type(a))

a='Do your homework'
print("Data type of a is:", type(a))

# 3. Sequence Data type(ordered): List, tuple, range
# list - mutable
# a= [1,2,3,4,5,5,5,5,5]
a = [5, 2, 1, 4, 3, 3, 3, 3]
print("From list:", a)

print(a[0])
print(a[4])
# print(a[5])
print("Data type of a is:", type(a))

a= ["one", "two", "three", "four", "five"]
print(a[1])
print(a[2])
print("Data type of a is:", type(a))

a= ["one", 2, "three", 4, 5]
print(a[1])
print(a[2])
print("Data type of a is:", type(a))

#tuple - immutable
print("***********TUPLE************")
a= (1,2,3,4,5)
print(a[0])
print(a[4])
# print(a[5])
print("Data type of a is:", type(a))

a= ("one", "two", "three", "four", "five")
print(a[1])
print(a[2])
print("Data type of a is:", type(a))

a= ("one", 2, "three", 4, 5)
print(a[1])
print(a[2])
print("Data type of a is:", type(a))

# range
for i in range(2,20):
    print(i, end=" ")

# 4. Set data type (un-ordered collections): set (mutable), frozenset (immutable)
# set_var= {1,2,3,4,5,5,5,5,5,5}
set_var = {5, 2, 1, 4, 3, 3, 3, 3}
# set_var.
print("From set:", set_var)
print(type(set_var))

froz_set_var = frozenset({1, 2, 3, 4, 5, 5, 5, 5, 5})

print(froz_set_var)
print(type(froz_set_var))

# 5. boolean data type - bool
bool_var = False
print(type(bool_var))

# 6. Mapping data type - dictionary
# key:value
dictObj = {"Name": "Neelam", "City": "Pune", "Pin": 411057, 23: "DOB"}
print(dictObj)
print(dictObj["Name"])
print(dictObj[23])

# *********************************************
# print vs input
# a= input("What is your roll number?")
# print(type(a))
# print("Roll nbr is:", a)

# a = float(input("Enter first number:"))
# b = float(input("Enter second number:"))
# print(type(a))
# print(type(b))
# print("Sum of these numbers:", a+b)
# Sum of 11 and 22 is:33

# print("Sum of", a, " and ", b, "is:\n", a + b)
#
# print(f"Sum of {a} and {b} is {a + b}")  # formatted string / f-string

str_url = "/EdWheel/Learning" #readable-format / r-string
app_url = r"https://www.google.com/asdsdsd?\sadd"
print(app_url)
print(str_url)