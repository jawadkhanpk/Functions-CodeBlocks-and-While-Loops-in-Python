# Function to add two numbers in Python
def add_numbers(a, b):
    return a + b


result = add_numbers(2, 5)
print(f"The sum of two numbers is: {result}")




# Function which will add two numbers entered by user

def add_numbers_entered_by_user(c, d):
    return c + d


number1 = int(input("Enter 1st Number: "))
number2 = int(input("Enter 2nd Number: "))

addition = add_numbers_entered_by_user(number1, number2)

print(f"The sum of c and d is: {addition}")
