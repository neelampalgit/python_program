import random

rand_integer = random.randint(0,1)
print(f"Randomly picked integer is:{rand_integer}")
if rand_integer==1:
    print("Heads")
else:
    print("Tails")

# picks up any decimal number between 0 and 1    (range 0.000000 and 0.99999999)
rand_float = random.random()
print(rand_float)

names = ['Angela','Bob', 'Neelam','Daniel']
print(random.choice(names))

#**************** Exercise ***********************
# Write a program that will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill
#*********************************************************************

print(len("Today is Monday"))