#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 10, 12, 9]), 12)
        self.assertEqual(max_integer([-20, -23, -9]), -9)
        self.assertEqual(max_integer([1, 10, 12, 9]), 12)
        self.assertEqual(max_integer([20, 19, 12, 9]), 20)
        self.assertEqual(max_integer([2.2, 1.2, 12.4, 9]), 12.4)
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([20, 19, 12, 9]), 20)
        self.assertEqual(max_integer([]), None)


if __name__ == '__main__':
    unittest.main()
