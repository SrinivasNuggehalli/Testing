# This file contains unit tests for all the mathematical functions implemented in scientific_calculator.py using Python's built-in unittest framework.
#
# The tests ensure that:
#
# Each mathematical function correctly computes the expected results for various valid inputs.
# Proper exceptions (TypeError, ValueError) are raised for invalid or non-numeric inputs.
# Tests are written for:

# Basic Trigonometric Functions (sin, cos, tan)
# Inverse Trigonometric Functions (asin, acos, atan)
# Hyperbolic Functions (sinh, cosh, tanh)
# Exponential and Logarithmic Functions (exp, log)
# Square Root Function (sqrt)

import unittest
import math
from scientific_calculator import sin, cos, tan, sqrt, log, exp, asin, acos, atan, sinh, cosh, tanh

class TestScientificCalculator(unittest.TestCase):

    # Tests for sin function
    def test_sin_positive(self):
        self.assertAlmostEqual(sin(90), 1.0, places=7)

    def test_sin_negative(self):
        self.assertAlmostEqual(sin(-90), -1.0, places=7)

    def test_sin_zero(self):
        self.assertEqual(sin(0), 0)

    def test_sin_non_numeric(self):
        with self.assertRaises(TypeError):
            sin("hello")

    # Tests for cos function
    def test_cos_positive(self):
        self.assertAlmostEqual(cos(0), 1.0, places=7)

    def test_cos_negative(self):
        self.assertAlmostEqual(cos(180), -1.0, places=7)

    def test_cos_zero(self):
        self.assertAlmostEqual(cos(90), 0, places=7)

    def test_cos_non_numeric(self):
        with self.assertRaises(TypeError):
            cos("hello")

    # Tests for tan function
    def test_tan_positive(self):
        self.assertAlmostEqual(tan(45), 1.0, places=7)

    def test_tan_negative(self):
        self.assertAlmostEqual(tan(-45), -1.0, places=7)

    def test_tan_zero(self):
        self.assertEqual(tan(0), 0)

    def test_tan_non_numeric(self):
        with self.assertRaises(TypeError):
            tan("hello")

    # Tests for sqrt function
    def test_sqrt_positive(self):
        self.assertEqual(sqrt(4), 2.0)

    def test_sqrt_zero(self):
        self.assertEqual(sqrt(0), 0.0)

    def test_sqrt_negative(self):
        with self.assertRaises(ValueError):
            sqrt(-4)

    def test_sqrt_non_numeric(self):
        with self.assertRaises(TypeError):
            sqrt("hello")

    # Tests for log function
    def test_log_positive(self):
        self.assertAlmostEqual(log(10), 2.3025851, places=7)  # Natural logarithm

    def test_log_zero(self):
        with self.assertRaises(ValueError):
            log(0)

    def test_log_negative(self):
        with self.assertRaises(ValueError):
            log(-1)

    def test_log_non_numeric(self):
        with self.assertRaises(TypeError):
            log("hello")

    # Tests for exp function
    def test_exp_positive(self):
        self.assertAlmostEqual(exp(1), 2.7182818, places=7)

    def test_exp_zero(self):
        self.assertEqual(exp(0), 1)

    def test_exp_negative(self):
        self.assertAlmostEqual(exp(-1), 0.3678794, places=7)

    def test_exp_non_numeric(self):
        with self.assertRaises(TypeError):
            exp("hello")
    
    # Tests for asin function
    def test_asin_valid(self):
        self.assertAlmostEqual(asin(1), math.pi / 2, places=7)

    def test_asin_negative(self):
        self.assertAlmostEqual(asin(-1), -math.pi / 2, places=7)

    def test_asin_invalid(self):
        with self.assertRaises(ValueError):
            asin(2)  # asin is only defined for values in the range [-1, 1]

    def test_asin_non_numeric(self):
        with self.assertRaises(TypeError):
            asin("hello")

    # Tests for acos function
    def test_acos_valid(self):
        self.assertAlmostEqual(acos(1), 0, places=7)

    def test_acos_negative(self):
        self.assertAlmostEqual(acos(-1), math.pi, places=7)

    def test_acos_invalid(self):
        with self.assertRaises(ValueError):
            acos(2)  # acos is only defined for values in the range [-1, 1]

    def test_acos_non_numeric(self):
        with self.assertRaises(TypeError):
            acos("hello")

    # Tests for atan function
    def test_atan_positive(self):
        self.assertAlmostEqual(atan(1), math.pi / 4, places=7)

    def test_atan_negative(self):
        self.assertAlmostEqual(atan(-1), -math.pi / 4, places=7)

    def test_atan_zero(self):
        self.assertEqual(atan(0), 0)

    def test_atan_non_numeric(self):
        with self.assertRaises(TypeError):
            atan("hello")

    # Tests for sinh function
    def test_sinh_positive(self):
        self.assertAlmostEqual(sinh(1), math.sinh(1), places=7)

    def test_sinh_negative(self):
        self.assertAlmostEqual(sinh(-1), math.sinh(-1), places=7)

    def test_sinh_zero(self):
        self.assertEqual(sinh(0), 0)

    def test_sinh_non_numeric(self):
        with self.assertRaises(TypeError):
            sinh("hello")

    # Tests for cosh function
    def test_cosh_positive(self):
        self.assertAlmostEqual(cosh(1), math.cosh(1), places=7)

    def test_cosh_negative(self):
        self.assertAlmostEqual(cosh(-1), math.cosh(-1), places=7)

    def test_cosh_zero(self):
        self.assertEqual(cosh(0), 1)

    def test_cosh_non_numeric(self):
        with self.assertRaises(TypeError):
            cosh("hello")

    # Tests for tanh function
    def test_tanh_positive(self):
        self.assertAlmostEqual(tanh(1), math.tanh(1), places=7)

    def test_tanh_negative(self):
        self.assertAlmostEqual(tanh(-1), math.tanh(-1), places=7)

    def test_tanh_zero(self):
        self.assertEqual(tanh(0), 0)

    def test_tanh_non_numeric(self):
        with self.assertRaises(TypeError):
            tanh("hello")

if __name__ == "__main__":
    unittest.main()

