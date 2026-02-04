# unittest - part of the stand library.
# - must subclass unittest.TestCase. 
# - TDD - test - fail - fail - pass
# - MAny assertion methods - use as many as you want - but only test one bit of logic per test. 
# - validating output is as expected. 
# - test_ - filenames + test cases. 
# - set-up + teardown. 
# - python3 -m unittest file_name || unittest. 


import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def test_calculator_class_exists(self):
        calc = Calculator() # make an instance of the class. 
        self.assertIsInstance(calc, Calculator) # test if calc is imstance of calculator.

    def test_add_method_exists(self):
        calc = Calculator()
        self.assertTrue(callable(getattr(calc, "add", None)))
    
    def test_input_validation(self):
        calc = Calculator()
        with self.assertRaisesRegex(TypeError, "numeric"):
            calc.add("a", 5)

    def test_add_method_performs_addition(self):
        calc = Calculator()
        self.assertEqual(calc.add(5, 5), 10)
        self.assertEqual(calc.add(500, 500), 1000)
        self.assertEqual(calc.add(-5, -5), -10)
        self.assertEqual(calc.add(0, 0), 0)


