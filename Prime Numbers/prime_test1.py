import unittest
from prime import prime_digit

class Prime_test(unittest.TestCase):

	def test_primes(self):
		self.assertEqual(prime_digit(7), [2,3,5,7])

if __name__=='__main__':
	unittest.main()