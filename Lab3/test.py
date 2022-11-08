import math
from typing import Type
import unittest
from funkcja_kwadratowa import function

class functionTest(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 1
        self.c = 1
        self.x_1 = 1

    def test_function(self):
        self.assertEqual(function(self.a, self.b, self.c, self.x_1, 1), 3.0)
        self.assertEqual(function(2, 2, 1, 1, 1), 5)
        self.assertEqual(function(-2, -2, -1, 2, 6), -13)

    def test_error(self):
        with self.assertRaises(TypeError):
            function("1", 1, 1, 1, 1)
        # with self.assertRaises(ValueError):
        #     function(0, 0, 0, 0, 0)




if __name__ == "__main__":
    unittest.main()