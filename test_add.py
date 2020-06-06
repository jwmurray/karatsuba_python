import unittest

from grade import add
from grade import sub
from grade import normalize_array

class add_test_case(unittest.TestCase):
    """Test add functionality"""

    def test_add_single_digits(self):
        """test adding 2 single digit strings"""
        sum = add([2], [3])
        self.assertEqual(sum, [5])

    def test_add_multiple_digits_with_carries(self):
        sum = add([2,5], [9,8])
        self.assertEqual(sum, [1,2, 3])
    def test_add_multiple_digits_with_middle_zero(self):
        sum = add([2,5], [7,8])
        self.assertEqual(sum, [1,0, 3])

    def test_sub_single_digit(self):
        sum = sub([5], [2])
        self.assertEqual(sum, [3])

    def test_sub_double_digit(self):
        sum = sub([5, 2], [2, 1])
        self.assertEqual(sum, [3, 1])
    def test_sub_single_digit_with_borrow(self):
        sum = sub([5], [7])
        self.assertEqual(sum, [-2])
    def test_sub_two_digit_with_borrow(self):
        sum = sub([1,5], [7])
        self.assertEqual(sum, [8])

    def test_normalize(self):
        array = normalize_array([1,5])
        self.assertEqual(array, [1,5])
        array = normalize_array([0,1,5])
        self.assertEqual(array, [1,5])
        array = normalize_array([0,-1,5])
        self.assertEqual(array, [-5])
        array = normalize_array([0,5,-1,5])
        self.assertEqual(array, [5,0,-5])
        array = normalize_array([0,1, 5,-1,5])
        self.assertEqual(array, [1,5,0,-5])
unittest.main()