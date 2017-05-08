import unittest
from prime import prime_digit

class Prime_test(unittest.TestCase):

	def test_generates_one_prime_for_input_2(self):
		self.assertEqual(prime_digit(2), [2])


if __name__=='__main__':
	unittest.main()