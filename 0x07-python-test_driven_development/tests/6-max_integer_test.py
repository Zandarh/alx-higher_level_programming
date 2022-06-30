#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """
        Class test for Max Number
        
    """
    def test_negative(self):
        """
            Checks if function can give the highest negative
            integer
        """
        self.assertEqual(max_integer([-0, -84, -1, -5]), 0)

    def test_positive(self):
        """
            Checks if function can give the highest positive
            integer
        """
        self.assertEqual(max_integer([9, 23, 76, 85]), 85)

    def test_positive_float(self):
        """
            Checks if function can give the highest positive
            float
        """
        self.assertEqual(max_integer([1.75, 3.25, 1.25, 5.8]), 5.8)

    def test_neg_float(self):
        """
            Checks if function can give the highest negative
            float
        """
        self.assertEqual(max_integer([-2.75, -4.25, -1.25, -5.5]), -1.25)

    def test_char(self):
        """
            Checks if function can give the highest negative
            float
        """
        self.assertEqual(max_integer(['a', 'b', 'c', 'd']), 'd')

    def test_if_list_empty(self):
        """Test for if list is empty"""

        self.assertIsNone(max_integer([]))

    def test_if_no_arg_received(self):
        """Test if no arguement is given"""

        self.assertIsNone(max_integer())
    
    def test_if_none_arg_received(self):
        """Test if none is the  arguement given"""

        self.assertRaises(TypeError, max_integer, None)

    def test_if_a_wrong_type_in_list(self):
        """Test for if a wrong type is provided"""

        self.assertRaises(TypeError, max_integer, [61, 2, "Alex"])

    def test_if_two_arg_received(self):
        """Test if two arguments given"""
        a = [1, 2, 5, 7]
        b = [3, 7, 8, 9]
        self.assertRaises(TypeError, max_integer, [3, 7, 8, 9], [1, 2, 5, 7])

    def test_if_a_int_type_passed(self):
        """Test for if a wrong type is provided"""

        self.assertRaises(TypeError, max_integer, 30)

    def test_if_a_dic_type_passed(self):
        """Test for if a wrong type is provided"""

        self.assertRaises(KeyError, max_integer, {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi"})




if __name__ == '__main__':
    unittest.main()    