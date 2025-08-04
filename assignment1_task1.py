'''
Ask the user to input three number and check if these numbers can form a triangle.
-> Need three inputs
-> The output shows whether the result can form a triangle or not
'''

#Take sides from user

side1=float(input("Enter first side:")) 
side2=float(input("Enter second side:"))
side3=float( input("Enter third side:"))

# by default sorts the input in asceding order
sides = sorted([side1,side2,side3])

# Now calculate if sum of smaller two sides > largest side

if sides[0] + sides[1] > sides[2]:
    print("Yes, they can form triangle")
else:
    print("NO, they cannot form triangle")
