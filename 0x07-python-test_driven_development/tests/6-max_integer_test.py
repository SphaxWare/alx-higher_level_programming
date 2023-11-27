#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInt(unittest.TestCase):
    """Unittest for max_integer([...])"""
    def test_no_arg(self):
        """Unittest for max_integer([...])"""
        self.assertEqual(max_integer(), None)

    def test_empty_list(self):
        """Test when an empty list is provided"""
        self.assertEqual(max_integer([]), None)

    def test_single_element_list(self):
        """Test when a list with a single element is provided"""
        self.assertEqual(max_integer([5]), 5)

    def test_positive_integers(self):
        """Test when a list of positive integers is provided"""
        self.assertEqual(max_integer([1, 3, 7, 2, 5]), 7)

    def test_negative_integers(self):
        """Test when a list of negative integers is provided"""
        self.assertEqual(max_integer([-1, -3, -7, -2, -5]), -1)

    def test_mixed_integers(self):
        """Test when a list of mixed positive
        and negative integers is provided"""
        self.assertEqual(max_integer([-1, 3, -7, 2, -5]), 3)

    def test_duplicate_max(self):
        """Test when the maximum value appears more than once in the list"""
        self.assertEqual(max_integer([3, 5, 7, 7, 2, 7]), 7)

    def test_floats(self):
        """Test when a list of floating-point numbers is provided"""
        self.assertEqual(max_integer([1.5, 2.7, 0.9, 2.7, 1.5]), 2.7)

    def test_mixed_types(self):
        """Test when the list contains mixed data
        types (integers and floats)"""
        self.assertEqual(max_integer([1, 2.5, 3, 4]), 4)

    def test_strings(self):
        """Test when the list contains strings"""
        self.assertEqual(max_integer(["apple", "orange", "banana"]), "orange")

    def test_mixed_types_with_strings(self):
        """Test when the list contains a mix of numbers and strings"""
        with self.assertRaises(TypeError):
            max_integer([1, "two", 3, "four"])

    def test_numeric_str(self):
        """Test for number as string"""
        self.assertEqual(max_integer("192834754"), "9")


if __name__ == '__main__':
    unittest.main()
