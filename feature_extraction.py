''''
	Feature Extraction - Technique(s) Implementation (without NLTK)
	===========================================================
	
	Feature extraction = process to generate a numeric representation of text data 
	using the Vector Space Model.
		The Vector Space Model, is defined as a mathematical and algebraic model for 
		transforming and representing text documents as numeric vectors of specific terms 
		that form the vector dimensions.

	Techniques:
		1. Bag of Words

'''

from collections import Counter
from normalization import get_gutenberg_data, tokenize
import pandas as pd


def bag_of_words(corpus, num_feats=50):
	""" BAG OF WORDS feature extraction technique.
		==========================================
		
		Given a list of text data get the freq distribution of tokens in a given document 
		based on the 'n' most common tokens amongst a collection of texts. 
		The resulting vector details the number of times the most common terms 
		in the entire collection appear in a specific document.

		
		Convert text documents into vectors s.t. the weight for each word is equal to its 
		frequency of occurrence in that document.

		
		Arguments:
			corpus {list} -- List of text data.
		
		Keyword Arguments:
			num_feats {number} -- Total number of features to extract. (default: {50})
		
		Returns:
			features {[Counter]} -- list of counter objects that represent vectors s.t. each vector represents 
									the frequency of all the distinct words that are present in the 
									 document vector space for that specific text.
			
			feature_name {set} -- set of feature names/labels (or words) associated with a given feature value.

	"""
	features = []
	feature_names, temp_feat_names = set(), Counter()
	texts = []

	# get unique words list from an amalgamation of all texts in collection
	for text in corpus:
		# get word list
		text_tokens = tokenize(text)
		# grow features list 
		#feature_names |= set(text_tokens)
		temp_feat_names.update(text_tokens)
		# add token list to text collection 
		texts.append(text_tokens)

	temp = temp_feat_names.most_common(num_feats)
	for k, v in temp:
		feature_names.add(k)

	# get features for each text in text collection
	for text in texts:
		curr_text = []
		for word in text:
			if word in feature_names:
				curr_text.append(word)
		features.append(Counter(curr_text))

	return features, feature_names


def print_features(features, feature_names):
	''' Matrix-like printing of bag of words feature vectors.
		=====================================================
	
		Arguments:
			features [list] -- list of vectors that correspond to a given feature label/value.
			feature_names [list] -- list of feature labels.
	'''
	df = pd.DataFrame(data=features, columns=feature_names)
	df.fillna(0, inplace=True)
	print df


if __name__ == "__main__":
	
	data = []

	data.append(get_gutenberg_data("https://www.gutenberg.org/files/2701/2701-0.txt", 6529, 1242147))
	data.append(get_gutenberg_data("https://www.gutenberg.org/files/2413/2413-0.txt", 1443, 666170))
	
	features, feature_names = bag_of_words(data, num_feats=10)
	print_features(features, feature_names)
