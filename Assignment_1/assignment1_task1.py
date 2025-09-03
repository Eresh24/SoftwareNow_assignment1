# Group 24 Assignment 1 Task 1

"""
Assignment 1 Task 1: Verify if three sides can form a triangle.

Our Understanding: To verify if three sides can form a triangle, we need to check the triangle inequality theorem:
1. The sum of the lengths of any two sides must be greater than the length of the third side.
2. All sides must be positive integers.
"""

# Function to verify if three sides can form a triangle
def verifyTriangle(a: int, b: int, c: int) -> None:
    if a <= 0 or b <= 0 or c <= 0:
        print("Sides must be positive numbers.")
        return

    if a + b > c and a + c > b and b + c > a:
        print(f"The sides {a}, {b}, and {c} can form a triangle.")
    else:
        print(f"The sides {a}, {b}, and {c} cannot form a triangle.")

# Function to get a valid integer input from the user
def getFloatInput(prompt: str) -> float:
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid positive number.")

# Main function to run the program
def main():
    print("Welcome to the Triangle Verifier! Group 24 Assignment 1 Task 1")
    a = getFloatInput("Enter the length of side a: ")
    b = getFloatInput("Enter the length of side b: ")
    c = getFloatInput("Enter the length of side c: ")

    verifyTriangle(a, b, c)

if __name__ == "__main__":  
    main()