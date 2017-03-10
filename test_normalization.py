import unittest
from normalization import tokenize, preprocess

class UtilitiesTestCase(unittest.TestCase):
	
	def test_normalize_text(self):
		self.assertEqual(preprocess("...This, is, a, SENTENCE."), 
			["this", "is", "a", "sentence"])

	def test_tokenize(self):
		self.assertEqual(tokenize("...This is a sentence. These are sentences!"), 
			["this", "is", "a", "sentence", "these", "are", "sentences"])


if __name__ == '__main__':
	unittest.main(verbosity=2)
