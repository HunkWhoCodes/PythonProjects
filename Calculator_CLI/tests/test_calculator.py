import unittest
import src.calculator as calculator

# This is necessary to use and test the functions
# To run use the following command:
# python -m unittest test_calculator

class TestCalculator(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(calculator.addition(10, 2), 12)
    
    def test_subtraction(self):
        self.assertEqual(calculator.subtract(10,2), 8)

    def test_multiplication(self):
        self.assertEqual(calculator.multiply(10,2), 20)

    def test_division(self):
        self.assertEqual(calculator.divide(10,2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10,0)
    
    def test_int_division(self):
        self.assertEqual(calculator.int_divide(10,2), 5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10,0)

    def test_exponent(self):
        self.assertEqual(calculator.power(10, 2), 100)

if __name__ == "__main__":
    unittest.main()             # Just to make sure script runs as the main program and no need to define main function as this already internally exists