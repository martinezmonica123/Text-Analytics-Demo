''''

	Simple term and bi-gram frequencies of (my favorite) top Gutenberg novels.
	=========================================================================

	Outline: 
		1. Gather Data:	
		2. Clean/Normalize Text
		3. Determine Word Counts
			a. compare w overall text word count
			b. bi-grams
		4. EXTRA: Determine usage overtime
			a. where in text are these words appearing most
			b. problem: how do you determine where a paragraph starts/ends?

	Novels: (7)
		-Emma by Jane Austen 
		-Adventures of Huckleberry Finn by Mark Twain 
		-Madame Bovary by Gustave Flaubert
		-Frankenstein; Or, The Modern Prometheus by Mary Wollstonecraft Shelley
		-Metamorphosis by Franz Kafka
		-Dracula by Bram Stoker
		-Moby Dick; Or, The Whale by Herman Melville

'''
import nltk 

from nltk.corpus import gutenberg
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

from os import path
from urllib import urlopen
from collections import Counter
import random

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud 


STOP_WORDS = set(stopwords.words('english')+["a", "the"]) # custom stop_words set
STOP_WORDS.update(set([x.strip() for x in open(
				path.join(path.dirname(__file__), 'data/stopwords.txt')).read().split('\n')])) # custom stop_words set

def get_data(url, start, end):
	data = urlopen(url).read().decode('utf8')
	data = data[start:end]
	return data

def tokenize_text(data):
	regex = RegexpTokenizer(r'\w+') #only takes alphanumeric sequences
	tokens = regex.tokenize(data)
	text = nltk.Text(tokens)
	return text

#TODO: remove trailing 's'
def normalize(data, stopwords=False):
	if stopwords:
		words = [w.lower() for w in data if w.lower() not in STOP_WORDS]
	else:
		words = [w.lower() for w in data]
	return words

#TODO: implement own bi-gram algorithm in utilities.py
def get_bigrams(data, stopwords=False):
	bigrams_data = nltk.bigrams(data)
	bigrams_list = list(bigrams_data)
	
	if stopwords:
		bigrams = [tup for tup in bigrams_list if not False in [False for w in tup if w in STOP_WORDS]]
		return Counter(bigrams)
	else:
		return Counter(bigrams_list)

def term_freq_dist(data, num):
	frequencies = {}
	term_total = float(len(data))
	terms = Counter(data)
	
	for term, count in terms.most_common(num):
		tf =(count/term_total)*100
		frequencies[term] = tf
	return frequencies

def pretty_print(data, title):
	print("%s: " % (title))
	for k,v in sorted(data.items()):
		if isinstance(k, tuple):
			print ("	%s %s - %.2f%%" % (k[0], k[1], v))
		else:
			print ("	%s - %.2f%%" % (k, v))
	print('\n')


def create_wordcloud(raw_data, title, bigrams=True):
	''' Generate Word Cloud -- Word_Cloud Library: https://github.com/amueller/word_cloud '''

	def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
	    return "hsl(0, 0%%, %d%%)" % random.randint(10, 60)
	    
	d = path.dirname(__file__)

	wordcloud = WordCloud(font_path=path.join(d, "fonts/raleway/raleway-light.ttf"), width=500, height=500, margin=20, background_color='white', max_words=20,
	               stopwords=STOP_WORDS, color_func=custom_color_func, random_state=20)
	
	wordcloud.collocations = bigrams
	wordcloud.generate(raw_data)

	default_colors = wordcloud.to_array()
	plt.title("Custom colors")
	plt.imshow(wordcloud)
	wordcloud.to_file("word_clouds/"+title+".png")
	print ('Created Word Cloud')

######################################################

if __name__ == '__main__':
	''' 
		Get Data, Tokenize, Normalize: Moby Dick - Example
		==================================================
	'''

	raw_data = get_data("https://www.gutenberg.org/files/2701/2701-0.txt", 6529, 1242147 )

	create_wordcloud(raw_data, 'Moby_Dick_WC')

	# word_data = normalize(tokenize_text(raw_data), True)
	# word_tf_data = term_freq_dist(word_data, 20)
	#pretty_print(word_tf_data, 'Terms')


	# bigram_data = normalize(tokenize_text(raw_data))
	# bigrams = get_bigrams(bigram_data, True)
	# bg_tf_data = term_freq_dist(bigrams, 20)
	# pretty_print(bg_tf_data, 'Bi-grams')


