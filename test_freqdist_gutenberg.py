import unittest
from freqdist_gutenberg import normalize


class UtilitiesTestCase(unittest.TestCase):
	
	def test_normalize(self):
		self.assertEqual(normalize("...This, is, a, SENTENCE."), ["this", "is", "a", "sentence"])


if __name__ == '__main__':
	unittest.main(verbosity=2)
