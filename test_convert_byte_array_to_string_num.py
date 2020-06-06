import unittest

from grade import convert_byte_array_to_string_number

class convert_byte_array_to_string_number_test_case(unittest.TestCase):
    """Test convert_byte_array_to_string_number functionality"""

    def test_convert_single_digits(self):
        """test converting 1 digit byte arrays"""
        string_num = convert_byte_array_to_string_number([2])
        self.assertEqual(string_num, "2")
        
    def test_convert_several_digits(self):
        """test convert several digit byte arrays"""
        string_num = convert_byte_array_to_string_number([1,2,3,4,5,6,7,8,9,0])
        self.assertEqual(string_num, "1234567890")

unittest.main()