# # List - Array - collection of data - mutable (changeable) - indexed
# numbers = [13, 2, 23, 53, 9]
# #           0  1   2   3  4
# print(numbers)
# print(numbers[3])

# numbers[2] = 17
# print(numbers)

# # print(numbers[5]) index out of range
# # numbers[5] = 72

# numbers.append(42)
# print(numbers)

# numbers.insert(3, 98)
# print(numbers)

# numbers.pop() 
# print(numbers)

# numbers.pop(2)
# print(numbers)

# numbers.remove(98)
# print(numbers)

# numbers.sort()
# print(numbers)

# numbers.reverse()
# print(numbers)


# numbers = [13, 2, 23, 53, 9, 23, 23, 53]

# print(numbers.count(23))
# print(numbers.index(9))
# print(len(numbers))


# Tuple - collection of data - indexed - immutable (cannot be changed)
names = ("John", "Jane", "Mike", "Jane", "Jane")
#           0       1       2       3       4
# names.append() cannot be done
# names[2] = "Simon" cannot be done
print(names)
print(type(names))

print(names.index("Mike"))
print(names.count("Jane"))
print(len(names))

days_of_the_week = ("Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday", "Sunday")
