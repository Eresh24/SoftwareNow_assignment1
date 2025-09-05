import turtle

def draw_edge(turtle_obj, length, depth):
    """
    Draw a single edge with recursive pattern.
    
    This function either draws a straight line (depth 0) or creates
    a pattern by dividing the line into 4 segments with an indentation.
    
    Parameters:
    - turtle_obj: The turtle object to draw with
    - length: How long the edge should be
    - depth: How many times to apply the pattern (0 = straight line)
    """
    
    # Base case: if depth is 0, just draw a straight line
    if depth == 0:
        turtle_obj.forward(length)
        return
    
    # Recursive case: create the pattern
    # Divide the line into 3 equal parts
    segment = length / 3
    
    # Draw the 4 segments that make up the pattern:
    # 1. First segment (1/3 of original length)
    draw_edge(turtle_obj, segment, depth - 1)
    
    # 2. Turn left and draw second segment (creates the indent)
    turtle_obj.left(60)
    draw_edge(turtle_obj, segment, depth - 1)
    
    # 3. Turn right and draw third segment (completes the indent)
    turtle_obj.right(120)
    draw_edge(turtle_obj, segment, depth - 1)
    
    # 4. Turn left to face original direction and draw final segment
    turtle_obj.left(60)
    draw_edge(turtle_obj, segment, depth - 1)


def get_number_input(prompt, min_val, max_val):
    """
    Get a number from user with error handling.
    
    Parameters:
    - prompt: What to ask the user
    - min_val: Minimum allowed value
    - max_val: Maximum allowed value
    
    Returns: A valid integer between min_val and max_val
    """
    while True:
        try:
            # Get input from user
            value = input(prompt)
            
            # Try to convert to integer
            number = int(value)
            
            # Check if it's in the valid range
            if min_val <= number <= max_val:
                return number
            else:
                print(f"Please enter a number between {min_val} and {max_val}")
                
        except ValueError:
            # This happens if user enters something that's not a number
            print("Please enter a valid number")
        except KeyboardInterrupt:
            # This happens if user presses Ctrl+C
            print("\nProgram cancelled by user")
            exit()


def draw_pattern():
    """
    Main function that gets user input and draws the pattern.
    """
    print("=" * 50)
    print("RECURSIVE POLYGON PATTERN GENERATOR")
    print("=" * 50)
    print("This program draws shapes where each edge has a repeating pattern.")
    print("The pattern creates indentations that repeat at smaller scales.")
    print()
    
    try:
        # Get input from user with error checking
        print("Let's set up your pattern:")
        print()
        
        sides = get_number_input(
            "How many sides should the shape have? (3-8): ", 
            3, 8
        )
        
        length = get_number_input(
            "How long should each side be? (100-400 pixels): ", 
            100, 400
        )
        
        depth = get_number_input(
            "How detailed should the pattern be? (0-3): ", 
            0, 3
        )
        
        print()
        print(f"Drawing a {sides}-sided shape...")
        print(f"Side length: {length} pixels")
        print(f"Pattern detail level: {depth}")
        print("Close the drawing window when you're done looking at it.")
        print()
        
        # Set up the drawing window
        screen = turtle.Screen()
        screen.setup(800, 600)  # Window size
        screen.bgcolor("white")
        screen.title(f"Koch Snowflake - {sides} sides, depth {depth}")
        
        # Create and set up the turtle
        pen = turtle.Turtle()
        pen.speed(5)  # Medium speed so you can see it draw
        pen.color("blue")
        pen.pensize(2)
        
        # Move to a good starting position
        pen.penup()
        pen.goto(-length//2, 0)  # Start a bit to the left of center
        pen.pendown()
        
        # Calculate how much to turn after each side
        angle = 360 / sides
        
        # Draw each side of the polygon
        for side_num in range(sides):
            print(f"Drawing side {side_num + 1}...")
            
            # Draw one side with the recursive pattern
            draw_edge(pen, length, depth)
            
            # Turn right to prepare for the next side
            pen.right(angle)
        
        print("Drawing complete!")
        print("Click on the drawing window to close it.")
        
        # Hide the turtle and wait for click to close
        pen.hideturtle()
        screen.exitonclick()
        
    except Exception as error:
        # Catch any unexpected errors
        print(f"Something went wrong: {error}")
        print("Please try running the program again.")
    
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        print("\nProgram stopped by user.")


# This is where the program starts running
if __name__ == "__main__":
    draw_pattern()