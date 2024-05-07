import math


def paint_calculator(height, width, cover):
    area = height * width
    number_of_cans = math.ceil(area / cover)  # math.ceil is used to round up decimal number to nearest integer
    print(f"You'll need {number_of_cans} cans of paint")


height_input = int(input("What is Height of a Wall: "))
width_input = int(input("What is Width of a Wall: "))

paint_calculator(height_input,width_input,cover=5)
