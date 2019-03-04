from HW05 import classify_triangle
import unittest

class CommonTest(unittest.TestCase):
    """A class that includes test methods that check classify_triangle() function."""

    def test_classify_triangle(self):
        """A method that tests what kind of triangle it is."""
        
        self.assertEqual(classify_triangle(4,4,4), "Equilateral")
        self.assertEqual(classify_triangle(3,4,5), "Scalene and Right.")
        self.assertEqual(classify_triangle(3,4,6), "Scalene")
        self.assertEqual(classify_triangle(4,4,6), "Isosceles")
        self.assertEqual(classify_triangle(7.071067812,7.071067812,10), "Isosceles and Right.")
        self.assertEqual(classify_triangle(3,4,9), "It is not a triangle.")
        self.assertEqual(classify_triangle(0,4,5), "Cannot have 0 as a side.")
        self.assertEqual(classify_triangle("bob", "blob", "f"), "Not a valid triangle.")
        self.assertEqual(classify_triangle("fdhs", 4, 4), "Not a valid triangle.")
        self.assertEqual(classify_triangle(-5, 4, 4), "It is not a triangle.")
        self.assertEqual(classify_triangle(5, -4, 4), "It is not a triangle.")
        self.assertEqual(classify_triangle(5, 4, -4), "It is not a triangle.")
        self.assertEqual(classify_triangle(1000000000000, 4000000003, 203030944949494), "It is not a triangle.")
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)