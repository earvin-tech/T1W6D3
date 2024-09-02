# factorial
# 6! = 6*5*4*3*2*1 = 720

num = int(input("Enter a number: "))
fact = 1

# for i in range(1, num + 1):
#     fact *= i

# print(fact)

for i in range(num, 0, -1):
    fact *= i
print(fact)