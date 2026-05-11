// Program: Area of a Trapezoid (Your Name)
// Created in MakeCode Arcade Python
// 1. Ask the user for the first base
let base1 = game.askForNumber("Enter Base 1:")
// 2. Ask the user for the second base
let base2 = game.askForNumber("Enter Base 2:")
// 3. Ask the user for the height
let height = game.askForNumber("Enter the Height:")
// 4. Calculate the area
// Formula: ((base1 + base2) / 2) * height
let area = (base1 + base2) / 2 * height
// 5. Display the result to the user
game.splash("The area is: " + ("" + area))
