''' Classification Algorithms Implementation
	========================================
	
	Classification algorithms are supervised machine learning algorithms that are
	used to classify, categorize, or label data points based on what it has observed in the past.

		Steps:
			1. Training
			2. Evaluation
			3. Tuning / Optimization

	Types: (for text analysis)
		1. Gaussian Naïve Bayes

'''

from feature_extraction import tf_idf, bag_of_words, feature_matrix, get_top_features
from data_scraping import read_csvfile