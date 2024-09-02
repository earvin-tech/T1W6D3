num1 = 5

num2 = num1 # copy by value

print(num1)
print(num2)

num1 = 7
print(num1)
print(num2)


list1 = [1, 2, 3]
list2 = list1 # copy by reference/address

print(list1)
print(list2)

list1.append(4)

print(list1)
print(list2)