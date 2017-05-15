''''
	Text Normalization Tools Implementation (without NLTK.)
	=====================================================

		1. Get data from file
		2. Normalize data
			a. case conversion
			b. remove newline characters
			c. remove punctuation
			d. remove stop-words
		3. Tokenize data
			a. sentence segmentation
			b. word tokenization
'''


#TODO: bi-gram support (maybe n-gram instead)
#TODO: variables for film script stop-words

from os import listdir, path
import re

# custom stop-words set
STOP_WORDS = set([x.strip() for x in open(path.join(path.dirname(__file__), 'data/other/stopwords.txt')).read().split('\n')])
SCRIPT = set()

#TODO: add stemming and lemmatization
#TODO: expand contractions
#TODO: correct spelling (from pattern.en import suggest from Pattern Library) AND look into algorithm
def preprocess(sentence, stopwords=True):
	''' Using simple raw text data: Perform case conversion; remove newline characters, punctuation, and stop-words. 
	'''
	# only extract alpha characters
	PATTERN = r'[^a-zA-Z]'

	sentence = sentence.lower().replace('\n', ' ')
	clean_sent = re.sub(PATTERN, r'', sentence)
	tokens = word_tokenize(clean_sent)

	if not stopwords:
		return tokens
	
	return [w for w in tokens if w not in STOP_WORDS]


def tokenize(text, stopwords=True):
	''' Word Tokenization of raw input data in 2 steps:
			1. Sentence Tokenization
			2. Text Normalization
			
			NLTK version: nltk.tokenize,RegexpTokenizer(r'\w+')
	'''
	result = []
	for item in sent_tokenize(text):
		# prevent empty sentences
		if item:
			tokens = preprocess(item)
			result.extend(tokens)
	return result


############################## Helper Functions ########################################


def word_tokenize(sentence):
	words = sentence.split()
	return words


def sent_tokenize(text):
	''' Sentence Extraction/Segmentation/Tokenizer:
			Splits sentences using end_of_sentence() function. 
			NLTK Version:  nltk.sent_tokenize
	'''
	start = 0
	sentences = []
	
	for end, char in enumerate(text):
		if end_of_sentence(char):
			sentence = text[start:end]
			sentences.append(sentence)
			start = end + 1
	return sentences


def end_of_sentence(char):
	''' Sentence tokenizer helper function:	Determine if character is an end of sentence delimiter.
	'''
	punct = ['!', '?', '.']
	return char in punct
