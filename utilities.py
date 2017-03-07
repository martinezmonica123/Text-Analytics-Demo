''''

	Text analysis tools without NLTK.
	=================================

'''

from os import listdir
import string


def read_file(filename):
	'''Read the contents of FILENAME and return as string'''
	infile = open(filename)
	contents = infile.read()
	infile.close()
	return contents

def list_textfiles(directory):
	'''Return a list of filenames ending in '.txt' in DIRECTORY'''
	textfiles = []
	for filename in listdir(directory):
		if filename.endswith(".txt"):
			textfiles.append(directory + "/" + filename)
	return textfiles

def split_words(text):
	words = text.split()
	return words

def end_of_sentence(char):
		punct = ['!', '?', '.']
		return char in punct

def split_sentences(text):
	start =  0
	sentences = []
	
	for end, char in enumerate(text):
		if end_of_sentence(char):
			sentence = text[start:end]
			sentences.append(sentence)
			start = end + 1
	
	return sentences

def clean_text(text):
	translator = str.maketrans('', '', string.punctuation)

	text = text.lower().replace('\n', ' ') # make lowercase and newline characters
	return text.translate(translator) # punctuation

def tokenize(text):
	result = []
	for item in split_sentences(text):
		if item: # prevent empty sentences
			sentence = clean_text(item)
			result.append(split_words(sentence))
	return result

##################################################################

if __name__ == '__main__':
    
	print (clean_text("...This, is, a, Sentence."))

	#text = read_file("data/austen-emma-excerpt.txt")

	#for item in tokenize(text):
	#	print (item)

	#print (len(split_sentences(text)))

	# for filepath in list_textfiles("data/gutenberg/training"):
	# 	text = read_file(filepath)
	# 	print(filepath + " has " + str(len(text)) + " characters.")
