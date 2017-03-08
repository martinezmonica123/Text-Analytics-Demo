''''

	Text analysis tools without NLTK.
	=================================

'''

from os import listdir, path
import string
import re

STOP_WORDS = set([x.strip() for x in open(
				path.join(path.dirname(__file__), 'data/stopwords.txt')).read().split('\n')]) # custom stop_words set

def read_file(filename):
	''' Read the contents of FILENAME and return as string'''
	infile = open(filename)
	contents = infile.read()
	infile.close()
	return contents

def list_textfiles(directory):
	''' Return a list of filenames ending in '.txt' in DIRECTORY'''
	textfiles = []
	for filename in listdir(directory):
		if filename.endswith(".txt"):
			textfiles.append(directory + "/" + filename)
	return textfiles

def word_tokenize(sentence):
	words = sentence.split()
	return words

def end_of_sentence(char):
	''' Sentence Tokenizer helper function:	
			Determine if character is an end of sentence 
			delimiter.
	'''
	punct = ['!', '?', '.']
	return char in punct

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

def normalize_text(sentence, stopwords=False):
	''' Using simple raw text data: Perform case conversion; remove newline characters, punctuation, and stop-words. 
			Does not support html file data.
		#TODO: add stemming and lemmatization
		#TODO: expand contractions
		#TODO: correct spelling (from pattern.en import suggest from Pattern Library) AND look into algorithm

	'''
	PATTERN = r'[^a-zA-Z0-9 ]' # only extract alpha-numeric characters

	sentence = sentence.lower().replace('\n', ' ') # case conversion and remove newline characters
	clean_sent = re.sub(PATTERN, r'', sentence) # remove punctuation by only extracting alpha-numeric characters
	tokens = word_tokenize(clean_sent) # word tokenization

	if not stopwords:
		return tokens
	
	return [w for w in tokens if w not in STOP_WORDS] #remove stop-words


def tokenize(text):
	''' Word Tokenization of raw input data in 2 steps:
			1. Sentence Tokenization
			2. Text Normalization
		NLTK version: nltk.tokenize,RegexpTokenizer(r'\w+')
	'''
	result = []
	for item in sent_tokenize(text):
		if item: # prevent empty sentences
			tokens = normalize_text(item)
			result.extend(tokens)
	return result

##################################################################

if __name__ == '__main__':
    
	print (normalize_text("...This, is, a, Sentence."))

	#text = read_file("data/austen-emma-excerpt.txt")

	#for item in tokenize(text):
	#	print (item)

	#print (len(sent_tokenize(text)))

	# for filepath in list_textfiles("data/gutenberg/training"):
	# 	text = read_file(filepath)
	# 	print(filepath + " has " + str(len(text)) + " characters.")
