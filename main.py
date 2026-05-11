# Program: Area of a Trapezoid (Your Name)
# Created in MakeCode Arcade Python
# 1. Ask the user for the first base
base1 = game.ask_for_number("Enter Base 1:")
# 2. Ask the user for the second base
base2 = game.ask_for_number("Enter Base 2:")
# 3. Ask the user for the height
height = game.ask_for_number("Enter the Height:")
# 4. Calculate the area
# Formula: ((base1 + base2) / 2) * height
area = (base1 + base2) / 2 * height
# 5. Display the result to the user
game.splash("The area is: " + ("" + str(area)))