fruits=('apple','banana', 'strawberry', 'orange', 'mango')
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
print("\n")
for _ in fruits:
    print(_)

# str_fruit = "banana"
# for fr in str_fruit:
#     print(fr, end="/")

for i in range(1,10):
    print(i)
    if i==5:
        break
    # print(i)

print("**************************WHILE*********")
i=1
while i<10:
    print(i)
    # i = i+1
    i += 1
    if i==5:
        continue
