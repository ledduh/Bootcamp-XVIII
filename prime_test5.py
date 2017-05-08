import unittest
from prime import prime_digit

class Prime_test(unittest.TestCase):

	def test_Raises_error_for_basstring_input(self):
		with self.assertRaises(TypeError):prime_digit("hello")


if __name__=='__main__':
	unittest.main()