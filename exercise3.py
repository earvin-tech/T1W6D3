# palindrome of a string

# string reversed is also the same as the original string

original_string = input("Enter a string: ")

reverse_string = ""

for character in original_string:
    reverse_string = character + reverse_string
print(reverse_string)

reverse_string_another_way = original_string[::-1]
print(reverse_string)

if reverse_string == original_string:
    print("palindrome")
else:
    print("not a palindrome")

if reverse_string_another_way == original_string:
    print("palindrome")
else:
    print("not a palindrome")