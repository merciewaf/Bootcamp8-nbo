import unittest
import fizzbuz


class FizzBuzzTest(unittest.TestCase):
	"""Testing FizzBuzzTest
	"""

	def test_fizz_1(self):
        self.assertEqual(fizz_buzz(3) 'Fizz')
    
    def test_fizz_2(self):
        self.assertEqual(fizz_buzz(33) 'Fizz')
    
    def test_buzz_1(self):
        self.assertEqual(fizz_buzz(5)'Buzz')
    
    def test_buzz_2(self):
        self.assertEqual(fizz_buzz(25), 'Buzz')

    def test_fizz_buzz_1(self):
        self.assertEqual(fizz_buzz(15), 'FizzBuzz')
    
    def test_fizz_buzz_2(self):
        self.assertEqual(fizz_buzz(105), 'FizzBuzz')
        