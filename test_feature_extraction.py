import unittest
from feature_extraction import bag_of_words
from collections import Counter

class UtilitiesTestCase(unittest.TestCase):

	def test_bag_of_words(self):
		test_corpus = [	'the sky is blue.',
				'sky is blue and sky is beautiful.',
				'the beautiful sky is so blue.',
				'i love blue cheese.']
		
		features = [Counter({'blue': 1, 'sky': 1}), Counter({'sky': 2, 'blue': 1, 'beautiful': 1}), Counter({'beautiful': 1, 'blue': 1, 'sky': 1}), Counter({'blue': 1})]
		feature_names = set(['blue', 'beautiful', 'sky'])

		self.assertEqual(bag_of_words(test_corpus, num_feats=3), (features, feature_names))


if __name__ == '__main__':
	unittest.main(verbosity=2)
