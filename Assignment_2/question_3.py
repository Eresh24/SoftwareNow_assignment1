'''
Create a program that uses a recursive function to generate a geometric pattern using
Python's turtle graphics. The pattern starts with a regular polygon and recursively
modifies each edge to create intricate designs.
Pattern Generation Rules:
For each edge of the shape:
1. Divide the edge into three equal segments
2. Replace the middle segment with two sides of an equilateral triangle pointing
inward (creating an indentation)
3. This transforms one straight edge into four smaller edges, each 1/3 the length of
the original edge
4. Apply this same process recursively to each of the four new edges based on the
specified depth
Visual Example:
Depth 0: Draw a straight line: ———— (no modification)
Depth 1: Line becomes: ——\⁄—— (indentation pointing inward)

Depth 2: Each of the 4 segments from depth 1 gets its own indentation
User Input Parameters:
The program should prompt the user for:
Number of sides: Determines the starting shape
Side length: The length of each edge of the initial polygon in pixels
Recursion depth: How many times to apply the pattern rules
Example Execution:
Enter the number of sides: 4
Enter the side length: 300
Enter the recursion depth: 3
'''

import turtle

# Recursive function to draw one edge with fractal indentation
def draw_fractal_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        segment = length / 3.0
        
        draw_fractal_edge(segment, depth - 1)
        
        turtle.left(60)
        draw_fractal_edge(segment, depth - 1)
        
        turtle.right(120)
        draw_fractal_edge(segment, depth - 1)
        
        turtle.left(60)
        draw_fractal_edge(segment, depth - 1)

def main():
    # User input
    sides = int(input("Enter the number of sides: "))
    side_length = int(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth (recommend ≤ 5): "))

    # Setup turtle
    turtle.speed(0)          # Fastest speed
    turtle.hideturtle()
    turtle.tracer(False)     # Disable animation for speed

    # Draw polygon with fractal edges
    for _ in range(sides):
        draw_fractal_edge(side_length, depth)
        turtle.right(360 / sides)

    turtle.tracer(True)      # Re-enable animation
    turtle.done()

if __name__ == "__main__":
    main()
