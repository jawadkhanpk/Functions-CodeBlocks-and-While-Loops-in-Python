def prime_no_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number!")
    else:
        print("It's not Prime Number!")


number_input = int(input("Check this Number: "))
prime_no_checker(number_input)
