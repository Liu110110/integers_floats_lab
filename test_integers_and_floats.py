from unittest import TestCase
from integers_and_floats import integer_division, float_integer_multiplication, inputs_are_strings

class Test(TestCase):
    def test_integer_division(self):
        self.assertEqual(integer_division(), type(2222/8.4))

    def test_float_integer_multiplication(self):
        self.assertEqual(float_integer_multiplication(), type(334*8.6))

    def test_inputs_are_strings(self):
        self.assertEqual(inputs_are_strings(), type(73 / 23))