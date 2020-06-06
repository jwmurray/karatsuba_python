import unittest

from grade import convert_string_number_to_byte_array

class convert_string_number_to_byte_array_test_case(unittest.TestCase):
    """Test convert_string_number_to_byte_array functionality"""

    def test_convert_single_digits(self):
        """test converting 1 digit strings"""
        array = convert_string_number_to_byte_array("2")
        self.assertEqual(array, [2])
        array = convert_string_number_to_byte_array("0")
        self.assertEqual(array, [0])

    def test_convert_2_digits(self):
            """test convert 2 digit strings"""
            array = convert_string_number_to_byte_array("23")
            self.assertEqual(array, [2, 3])

    def test_convert_several_digits(self):
            """test convert 2 digit strings"""
            array = convert_string_number_to_byte_array("1234567890")
            self.assertEqual(array, [1,2, 3,4,5,6,7,8,9,0])

unittest.main()