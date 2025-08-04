# Group 24 Assignment 1 Task 2

"""
Assignment 1 Task 2: Draw a hollow square of a given size.

Our Understanding: To draw a hollow square, we need to print asterisks (*) for the borders and spaces for the inner part of the square.
"""
# Function to draw a hollow square of given size 
def drawSquare(size: int) -> None:
    for row in range(size):
        for col in range(size):
            if row in (0, size - 1) or col in (0, size - 1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Function to get user input for the size of the square
def getUserInput() -> int:
    while True:
        user_input = input("Enter a positive number (or 'q' to quit): ").strip().lower()

        # Check if the user wants to quit
        if user_input == 'q':
            return None
        # Validate the input to ensure it's a positive integer
        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                return number
            else:
                print("Please enter a number greater than zero.")
        else:
            print("Invalid input. Please enter a valid positive number or 'q' to quit.")

# Main function to run the program
def main():
    print("Welcome to the Hollow Square Drawer! Group 24 Assignment 1 Task 2")
    while True:
        size = getUserInput()
        if size is None:
            print("Exiting the program. Goodbye!")
            break
        drawSquare(size)

if __name__ == "__main__":  
    main()