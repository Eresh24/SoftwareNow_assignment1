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
import matplotlib.pyplot as plt
import math

def draw_koch_segment(x0, y0, x1, y1, depth, coords):
    """Recursively compute points for a Koch segment"""
    if depth == 0:
        coords.append((x1, y1))
        return
    
    dx = (x1 - x0) / 3
    dy = (y1 - y0) / 3
    
    xA, yA = x0, y0
    xB, yB = x0 + dx, y0 + dy
    xD, yD = x0 + 2*dx, y0 + 2*dy
    xE, yE = x1, y1
    
    # Peak of the triangle
    angle = math.atan2(dy, dx) - math.pi/3
    length = math.hypot(dx, dy)
    xC = xB + math.cos(angle) * length
    yC = yB + math.sin(angle) * length
    
    draw_koch_segment(xA, yA, xB, yB, depth-1, coords)
    draw_koch_segment(xB, yB, xC, yC, depth-1, coords)
    draw_koch_segment(xC, yC, xD, yD, depth-1, coords)
    draw_koch_segment(xD, yD, xE, yE, depth-1, coords)

def draw_koch_polygon(sides, length, depth):
    """Draw a Koch polygon and display it in a window"""
    angle = 2 * math.pi / sides
    radius = length / (2 * math.sin(math.pi / sides))
    
    vertices = []
    for i in range(sides):
        x = radius * math.sin(i * angle)
        y = -radius * math.cos(i * angle)
        vertices.append((x, y))
    
    all_coords = []
    for i in range(sides):
        x0, y0 = vertices[i]
        x1, y1 = vertices[(i+1)%sides]
        edge_coords = [(x0, y0)]
        draw_koch_segment(x0, y0, x1, y1, depth, edge_coords)
        all_coords.extend(edge_coords)
    
    X, Y = zip(*all_coords)
    
    plt.figure(figsize=(8, 8))
    plt.plot(X, Y, color="blue")
    plt.axis("equal")
    plt.axis("off")
    plt.show()  # Display the window

def main():
    print("Geometric Pattern Generator")
    sides = int(input("Enter the number of sides: "))
    length = float(input("Enter the side length: "))
    depth = int(input("Enter the recursion depth: "))
    
    draw_koch_polygon(sides, length, depth)

if __name__ == "__main__":
    main()
