import unittest

from grade import mult

class mult_test_case(unittest.TestCase):
    """Tests mult functionality"""

    def test_mult_single_digits(self):
        """Does single digit multiplication work?"""
        product = mult([4], [5])
        self.assertEqual(product, [2,0])

    def test_mult_null_string_against_single_digit(self):
        """Does single digit multiplication work with one digit None?"""
        product = mult([], [5])
        self.assertEqual(product, None)

    def test_mult_1x2_digits(self):
            product = mult([4], [1,0])
            self.assertEqual(product, [4,0])
            product = mult([4,5], [8])
            self.assertEqual(product, [3,6,0])
            
    def test_mult_2x2_digits(self):
        product = mult([1,2], [3,1])
        self.assertEqual(product, [3,7,2])
    
    def test_mult_2x2_with_carry_digits(self):
        product = mult([8,9], [6,7])
        self.assertEqual(product, [5,9,6,3])

    def test_mult_3x3_with_carry_digits(self):
        product = mult([1,0,1], [1,2,9])
        self.assertEqual(product, [1,3,0,2,9])

    def test_mult_4x4_digits(self):
        product = mult([8,9,1,2], [9,8,3,1])
        self.assertEqual(product, [8,7,6,1,3,8,7,2])

    def test_mult_8x8_digits(self):
        product = mult([4,5,6,0,0,0,0,0], [4,5,6,0,0,0,0,0])
        self.assertEqual(product, [2,0,7,9,3,6,0,0,0,0,0,0,0,0,0,0])

    def test_mult_9x9_digits(self):
        product = mult([4,5,6,0,0,0,0,0,0], [4,5,6,0,0,0,0,0,0])
        self.assertEqual(product, [2,0,7,9,3,6,0,0,0,0,0,0,0,0,0,0,0,0])

    # def test_mult_3_digits(self):
    #     product = mult([8,9,2], [4, 3,5])
    #     self.assertEqual(product, [3,8,8,0,2,0])


unittest.main()