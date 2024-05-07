def greet_user(name,city):
    print(f"\nHello {name}!")
    print(f"How is the weather in {city}?")

name = input("What is Your Name: ")
city = input("What is Your City Name: ")

greet_user(name,city)