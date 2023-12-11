import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_size_property(self):
        s = Square(2, 3, 4, 1)
        self.assertEqual(s.size, 2)

    def test_size_setter(self):
        s = Square(2, 3, 4, 1)
        s.size = 5
        self.assertEqual(s.size, 5)
        self.assertEqual(s.width, 5)
        self.assertEqual(s.height, 5)

    def test_str(self):
        s = Square(2, 3, 4, 1)
        self.assertEqual(str(s), '[Square] (1) 3/4 - 2')

    def test_update(self):
        s = Square(2, 3, 4, 1)
        s.update(10, 20, 30, 40)
        actual = str(s)
        expected = '[Square] (10) 30/40 - 20'
        self.assertEqual(actual, expected, f'Actual: {actual}')

    def test_to_dictionary(self):
        s = Square(2, 3, 4, 1)
        self.assertEqual(s.to_dictionary(), {'id': 1, 'size': 2, 'x': 3, 'y': 4})


if __name__ == '__main__':
    unittest.main()
