# If a number is prime 
# prime number is a number that is divisible by 1 and itself only


number = int(input("Enter a number: "))

for i in range(2, number):
    if number % i == 0:
        print("Not a prime")
        break
else:
    print("A prime")