import unittest
from prime import prime_digit

class Prime_test(unittest.TestCase):

	def test_primes(self):
		self.assertEqual(prime_digit(7), [2,3,5,7])

	def test_Raises_error_for_input_zero(self):
		with self.assertRaises(ValueError):prime_digit(0)

	def test_Raises_error_for_negative_input(self):
		with self.assertRaises(ValueError):prime_digit(-1)

	def test_Raises_error_for_dict_input(self):
		with self.assertRaises(TypeError):prime_digit({})

	def test_generates_one_prime_for_input_2(self):
		self.assertEqual(prime_digit(2), [2])

	def test_Raises_error_for_basstring_input(self):
		with self.assertRaises(TypeError):prime_digit("hello")


if __name__=='__main__':
	unittest.main()