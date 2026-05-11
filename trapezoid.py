# Program: Area of a Trapezoid colden

print("--- Area of a Trapezoid Calculator ---")

# 1. Get user inputs
# We use float() so the user can enter decimals (like 5.5)
base1 = float(input("Enter the first base (b1): "))
base2 = float(input("Enter the second base (b2): "))
height = float(input("Enter the height (h): "))

# 2. Calculate the area
# Formula: ((b1 + b2) / 2) * h
area = ((base1 + base2) / 2) * height

# 3. Display the result
print(f"\nThe area of the trapezoid is: {area}")