login_attempts = 5

while login_attempts > 0:
    password = input("Enter your password: ")
    if password != "hello":
        print("Password incorrect")
        login_attempts -= 1
        print(f"Remaining attempts: {login_attempts}")
    else:
        print("Login Successful")
        break