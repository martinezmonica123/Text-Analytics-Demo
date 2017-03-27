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
		2. TF-IDF Model

'''

from collections import Counter, defaultdict
from normalization import get_gutenberg_data, tokenize
import pandas as pd
import math


def bag_of_words(corpus, num_feats=50, for_tf_idf=False):
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
			num_feats {int} -- Total number of features to extract. (default: {50})
			for_tf_idf {bool} -- Specify if being used for tf_idf calculations, 
								if true return additional data. (default: {False}) 
		
		Returns:
			features {[Counter]} -- word counts of each doc in corpus;
									list of counter objects that represent vectors s.t. each vector represents 
									the frequency of all the distinct words that are present in the 
									 document vector space for that specific text.
			
			feature_name {set} -- the set of words across all docs;
								set of feature names/labels (or words) associated with a given feature value. 
	"""
	features = []
	feature_names, temp_feat_names = set(), Counter()
	texts = []
	term_counts = [] 

	# get unique words list from an amalgamation of all texts in collection
	for text in corpus:
		# get word list
		text_tokens = tokenize(text)
		#get word counts 
		term_counts.append(len(text_tokens))

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

	#if data being used for tf-idf then also return term counts for each document
	if for_tf_idf:
		return features, term_counts
	
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


def tf(word, doc_index, term_counts, features):
	''' Term Frequency:
		
		TF = # term appears in doc / total terms in doc

		Using the bag or words model returns the number of times a given 'word'
		appears in a given document divided by the total number of words in that document.
		
		Arguments:
			word [string] -- the term
			doc_index [int] -- the index location of the target document in given 'features' collection
			features [list] -- list of counter objects that 
								contain term frequencies as produced by bag of words function.
		
		Returns:
			[int] -- the term frequency of a word in a particular document
	'''
	return (features[doc_index][word] / float(term_counts[doc_index]))


def idf(word, all_features):
	''' Inverse Document Frequency:
			 	
	 	LOG (	   C 	  )
	 		(  ---------- )
	 		(	1 + DF(T) )

		The inverse of the document frequency for each term
		
		Arguments:
			word [string] -- the word
			all_features [counter] -- list of counter objects that represent 
									the term frequencies of all documents.
		
		Returns:
			idf [int] -- the log of the total number of docs divided 
							by the document frequency of each term.		
	'''
	#the number of documents that contain 'word'
	df = float(sum(1 for doc in all_features if word in doc))
	
	#the total number of docs in collection
	count = float(len(all_features))

	idf = 1 + math.log((count / (1 + df)), 10)
	return idf


#TODO: tf_idf for all term in all documents -- matrix style
#TODO: Euclidean norm
def tf_idf(word, doc_index, term_counts, features):
	'''Term Frequency-Inverse Document Frequency:
		A way to score the importance of words in a document based on how frequently
		it appears across multiple documents.

			TF-IDF = 	TF 
					-----------
				 	1 + LOG 	C
				 			---------
				 			1 + DF(T)
				TF = word counts (what is computed using bag of words)
				DF = the number of documents that contain a given word
				C = number of documents in corpus
			
			[to normalize: use euclidean norm aka the square root 
			of the sum of the square of each term's tf-idf]

		If a word appears frequently in a document it's important
		BUUUT
		if a word appears in MANY documents then it is not a unique identifier.

		Arguments:
			word [string] -- the word to analyze
			doc_index [int] -- the index of the document to analyze
			term_counts [list] -- list of term counts of each document
			features [list] -- list of counter objects
		Returns:

	'''
	return tf(word, doc_index, term_counts, features) * idf(word, features)


if __name__ == "__main__":
	
	data = ['the big big truck is super far from me and my car.', 'the big big car is super far from me and my car.']

	# data.append(get_gutenberg_data("https://www.gutenberg.org/files/2701/2701-0.txt", 6529, 1242147))
	# data.append(get_gutenberg_data("https://www.gutenberg.org/files/2413/2413-0.txt", 1443, 666170))
	
	features, term_counts = bag_of_words(data, num_feats=5, for_tf_idf=True)
	
	# print_features(features, feature_names)
	# print(tf_idf('big', 0, term_counts, features))

