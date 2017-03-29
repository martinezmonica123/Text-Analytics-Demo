'''' Feature Extraction - Technique(s) Implementation (without NLTK)
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


def initialize_vsm(corpus):
	#generate corpus vocabulary
	vocab = generate_vocabulary(corpus)

	#initialize vector space
	docs = {}
	for i, doc in enumerate(corpus):
		name = 'd' + str(i)
		docs[name] = {'tokens': [], 'count': {}, 'tf': {}, 'idf': {}, 'tf-idf': {}}
		docs[name]['tokens'].extend(tokenize(doc))
	return vocab, docs


#TODO: MAKE SUCH THAT ONLY N FEATUERS EXTRACTED
#TODO: UPDATE FUNCTION DESCRIPTION
def bag_of_words(corpus):
	""" BAG OF WORDS feature extraction technique.
		==========================================
		
		[ADD DESCRIPTION]
		
		Arguments:
			corpus {list} -- List of text data.

		Returns:
			docs {dictionary} -- the vector space representation of docs in corpus.
									dictionary that specifies the tokens and token_counts per doc in corpus.
									docs = {d1: tokens': [], 'count': {}, ... , dn: tokens': [], 'count': {}}
			vocab {set} -- the set of words across all docs;
								set of feature names/labels (or words) associated with a given feature value. 
	"""
	vocab, docs = initialize_vsm(corpus)

	#update vector model with term counts as per bag-of-words model
	for doc in docs:
		token_list = docs[doc]['tokens']
		counts = get_count(token_list)
		for token in vocab:
			if token in token_list:
				docs[doc]['count'][token] = counts[token]
			else:
				docs[doc]['count'][token] = 0
	return vocab, docs


#TODO: MAKE SUCH THAT ONLY N FEATUERS EXTRACTED
#TODO: Euclidean norm
def tf_idf(corpus):
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
	vocab, docs = initialize_vsm(corpus)
	
	#update vector model with as per tf-idf model
	for doc in docs:
		token_list = docs[doc]['tokens']
		for token in token_list:
			docs[doc]['tf'][token] = tf(token, token_list)
			docs[doc]['idf'][token] = idf(token, docs)
			docs[doc]['tf-idf'][token] = docs[doc]['tf'][token] * docs[doc]['idf'][token]
	
	return vocab, docs


# ------------------------ HELPER FUNCTIONS ------------------------


def print_features(docs, vocab, bow=False, tfidf=False):
	''' Matrix-like printing of feature vectors.
		=====================================================
	
		Arguments:
			docs [dictionary] -- list of vectors that correspond to a given feature label/value.
			vocab [list] -- list of feature labels.
		Keyword Arguments:
			bow [bool] -- aka Bag of Words: specifies the type of data  {default: False}
			tfidf [bool] -- aka TF-IDF: specifies the type of data {default: False}
	'''
	features = []
	for doc in docs:
		counts = docs[doc]['count']
		tf_idf = docs[doc]['tf-idf']
		
		if bow:
			features.append(counts)
		elif tfidf:
			features.append(tf_idf)

	df = pd.DataFrame(data=features, columns=vocab, index=docs)
	df.fillna(0, inplace=True)
	print df


#TODO: UPDATE FUNCTION DESCRIPTION
def generate_vocabulary(docs):
	#unique vocab list across all docs
	vocab = set()
	for doc in docs:
		tokens = tokenize(doc)
		vocab.update(tokens)
	return vocab


#TODO: UPDATE FUNCTION DESCRIPTION
def get_count(tokens):
	counts = Counter(tokens)
	return counts


#TODO: UPDATE FUNCTION DESCRIPTION
def tf(word, tokens):
	count = get_count(word, tokens)
	total_count = len(tokens)
	return (count / float(total_count))


#TODO: UPDATE FUNCTION DESCRIPTION
def idf(word, docs):
	#number of docs containing 'word'
	df = float(sum(1 for doc in docs if word in docs[doc]['tokens']))
	#number documents in collection
	c = len(docs)
	return (1 + math.log10((c) / (1 + df)))


#TODO: DOCUMENT
def get_top_features(docs, num, type):
	'''[summary]
	
		[description]
		
		Arguments:
			docs [dictionary] -- [description]
			num [int] -- [description]
			type [string] -- [description]
		Returns:
			temp [Counter]
	'''
	if type == 'bow':
		for d in docs:
			bow = docs[d]['count']
			top = Counter(bow).most_common(num)
	
	elif type == 'tfidf':
		for d in docs:
			tfidf = docs[d]['tf-idf']
			top = Counter(tfidf).most_common(num)
	
	return(top)


if __name__ == "__main__":
	
	# data = ['the big big truck is super far from me and my car.', 'the big big car is super far from me and my car.']

	data = []
	data.append(get_gutenberg_data("https://www.gutenberg.org/files/2701/2701-0.txt", 6529, 1242147))
	data.append(get_gutenberg_data("https://www.gutenberg.org/files/2413/2413-0.txt", 1443, 666170))
	
	# vocab, docs = tf_idf(data)
	vocab, docs = bag_of_words(data)
	
	print(get_top_features(docs, 10, 'bow'))

	# print_features(docs, vocab, bow=True)
	# print(tf_idf('big', 0, term_counts, features))