"""Ekaterina (Katya) Bevinova
   SSW-567-A
"""

def classify_triangle(a,b,c):
    """A function that tells if the triangle is Equilateral, Isosceles, Scalene and possibly right."""

    try:
        float(a) and float(b) and float(c)

        if a == 0 or b == 0 or c == 0:
            return "Cannot have 0 as a side."
        elif (a + b <= c) or (a + c <= b) or (b + c <= a): 
            return "It is not a triangle."
        elif a == b == c:
            return "Equilateral"
        elif (a == b or b ==c or a == c) and round(a**2 + b**2) == c**2:
            return "Isosceles and Right."
        elif a == b or b ==c or a == c:
            return "Isosceles"
        elif a != b != c and a**2 + b**2 == c**2:
            return "Scalene and Right."
        elif a != b != c:
            return "Scalene"
        else:
            return "It is not a triangle."

    except ValueError:
        return "Not a valid triangle."

    
def main():
    print(classify_triangle(3,4,5))

if __name__ == '__main__':
    main()

