'''
Ask the user to input three numbers and check if these numbers can form a triangle.
-> Need three inputs
-> The output shows whether the result can form a triangle or not
'''

# Take sides from user
side1 = float(input("Enter first side: ")) 
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))

# Check that all sides are positive
if side1 <= 0 or side2 <= 0 or side3 <= 0:
    print("Invalid input: All sides must be positive numbers.")
else:
    # Sort the sides in ascending order
    sides = sorted([side1, side2, side3])

    # Check if the sum of the two smaller sides is greater than the largest
    if sides[0] + sides[1] > sides[2]:
        print("Yes, they can form a triangle.")
    else:
        print("No, they cannot form a triangle.")
