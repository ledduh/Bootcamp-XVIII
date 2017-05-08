import unittest
from prime import prime_digit

class Prime_test(unittest.TestCase):

	def test_Raises_error_for_negative_input(self):
		with self.assertRaises(ValueError):prime_digit(-1)

if __name__=='__main__':
	unittest.main()