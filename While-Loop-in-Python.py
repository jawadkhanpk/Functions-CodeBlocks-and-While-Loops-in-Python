count = 5
while count > 0:  # This means condition is true, while loop runs when condition is true
    print(count)
    count -= 1

# While loop to verify password

password = "pakistan123"
while True:
    user_password = input("Enter Password: ")
    if user_password == password:
        print("Password Matched!")
        break
    else:
        print("Incorrect Password! Please Try Again")