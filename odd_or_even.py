# List all numbers between 10 and 100, and state whether they are odd or even (100 exclusive)

for num in range(10,100):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")