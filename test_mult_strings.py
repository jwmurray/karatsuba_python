import unittest

from grade import mult_strings

class mult_strings_test_case(unittest.TestCase):
    """Test mult_strings functionality"""

    def test_mult_strings_single_digits(self):
        """test converting 1 digit byte arrays"""
        string_num = mult_strings("2","4")
        self.assertEqual(string_num, "8")
        
    def test_mult_strings_single_digits_with_carry(self):
        """test converting 1 digit byte arrays"""
        string_num = mult_strings("5","4")
        self.assertEqual(string_num, "20")
    

unittest.main()