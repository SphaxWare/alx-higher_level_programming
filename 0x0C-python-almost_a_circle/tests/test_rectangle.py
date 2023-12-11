import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.area(), 6)

    def test_display(self):
        r = Rectangle(2, 3)
        self.assertEqual(r.display(), None)  # Assuming display method prints to console

    def test_str(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(str(r), '[Rectangle] (1) 4/5 - 2/3')

    def test_update(self):
        r = Rectangle(2, 3, 4, 5, 1)
        r.update(10, 20, 30, 40, 50)
        self.assertEqual(str(r), '[Rectangle] (10) 40/50 - 20/30')

    def test_to_dictionary(self):
        r = Rectangle(2, 3, 4, 5, 1)
        self.assertEqual(r.to_dictionary(), {'id': 1, 'width': 2, 'height': 3, 'x': 4, 'y': 5})


if __name__ == '__main__':
    unittest.main()
