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
import math

def draw_koch_segment(t, x0, y0, x1, y1, depth):
    """Recursively draw a Koch segment with INWARD indentations using Turtle"""
    if depth == 0:
        t.goto(x1, y1)
        return

    # Divide the segment into three equal parts
    dx = (x1 - x0) / 3
    dy = (y1 - y0) / 3

    # Calculate the five key points
    xA, yA = x0, y0                    # Start point
    xB, yB = x0 + dx, y0 + dy          # First 1/3 point
    xD, yD = x0 + 2*dx, y0 + 2*dy      # Second 2/3 point
    xE, yE = x1, y1                    # End point

    # Calculate the peak of the triangle (pointing INWARD)
    # For inward triangle, we rotate by +60 degrees (π/3) instead of -60 degrees
    angle = math.atan2(dy, dx) + math.pi / 3  # Changed from - to + for inward
    length = math.hypot(dx, dy)
    xC = xB + math.cos(angle) * length
    yC = yB + math.sin(angle) * length

    # Recursively draw the four segments
    draw_koch_segment(t, xA, yA, xB, yB, depth - 1)  # First segment
    draw_koch_segment(t, xB, yB, xC, yC, depth - 1)  # Left side of triangle
    draw_koch_segment(t, xC, yC, xD, yD, depth - 1)  # Right side of triangle
    draw_koch_segment(t, xD, yD, xE, yE, depth - 1)  # Last segment

def draw_koch_polygon(sides, length, depth):
    """Draw a Koch polygon with inward indentations"""
    # Calculate the radius of the circumscribed circle
    angle = 2 * math.pi / sides
    radius = length / (2 * math.sin(math.pi / sides))

    # Calculate vertices of the regular polygon
    # Add a rotation offset to align the polygon properly
    # For a square, rotate by π/4 (45 degrees) to make it sit flat
    rotation_offset = math.pi / 4  # 45 degrees clockwise rotation
    vertices = []
    for i in range(sides):
        x = radius * math.sin(i * angle + rotation_offset)
        y = -radius * math.cos(i * angle + rotation_offset)
        vertices.append((x, y))

    # Setup Turtle graphics
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("white")
    screen.title(f"Inward Koch Pattern - {sides} sides, depth {depth}")
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest drawing speed
    t.color("black")
    t.pensize(1)
    
    # Start drawing from the first vertex
    t.penup()
    t.goto(vertices[0])
    t.pendown()

    # Draw each edge of the polygon with Koch modification
    for i in range(sides):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i + 1) % sides]
        draw_koch_segment(t, x0, y0, x1, y1, depth)

    t.hideturtle()
    
    # Keep the window open
    screen.exitonclick()
    print("Click on the graphics window to close it.")

def main():
    """Main function to get user input and generate the pattern"""
    print("Geometric Pattern Generator (Inward Koch Pattern)")
    print("=" * 50)
    
    try:
        sides = int(input("Enter the number of sides: "))
        if sides < 3:
            print("Number of sides must be at least 3!")
            return
            
        length = float(input("Enter the side length: "))
        if length <= 0:
            print("Side length must be positive!")
            return
            
        depth = int(input("Enter the recursion depth: "))
        if depth < 0:
            print("Recursion depth must be non-negative!")
            return
            
        print(f"\nGenerating pattern with:")
        print(f"- Sides: {sides}")
        print(f"- Side length: {length}")
        print(f"- Recursion depth: {depth}")
        print("\nDrawing pattern... Please wait.")
        
        draw_koch_polygon(sides, length, depth)
        
    except ValueError:
        print("Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()