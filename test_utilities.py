import unittest
from utilities import tokenize, clean_text

class UtilitiesTestCase(unittest.TestCase):
	
	def test_clean_text(self):
		self.assertEqual(clean_text("...This, is, a, Sentence."), "this is a sentence")

	def test_tokenize(self):
		self.assertEqual(tokenize("...This is a sentence."), [["this", "is", "a", "sentence"]])


if __name__ == '__main__':
	unittest.main(verbosity=2)