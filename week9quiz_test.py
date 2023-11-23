import unittest
from week9inclassquizz import Rectangle 
from week9inclassquizz import Circle

class TestCircleArea(unittest.TestCase):
    def test_circle_area(self):
        circle_instance = Circle(5)
        circle_expected_area = 3.14 * 5 ** 2

        self.assertEqual(circle_instance.area(), circle_expected_area)

class TestRectangleArea(unittest.TestCase):
    def test_rectangle_area(self):
        rectangle_instance = Rectangle(2,3)
        rectangle_expected_area = 2*3

        self.assertEqual(rectangle_instance.area(), rectangle_expected_area)

if __name__ == '__main__':
    unittest.main()