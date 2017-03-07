''''
Simple word and bi-gram frequencies of top Gutenberg novels.

Outline: 
	1. Gather Data:	
	2. Clean/Normalize Text
	3. Determine Word Counts
		a. compare w overall text word count
		b. most vs least used
	4. Determine usage overtime
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
from nltk import bigrams

from urllib import urlopen
from collections import Counter


raw = urlopen("https://www.gutenberg.org/files/2413/2413-0.txt").read().decode('utf8')
raw = raw[1443:666170] #Madame Bovary

# TOKENIZE 
regextokenzr = RegexpTokenizer(r'\w+') #only takes alphanumeric sequences
tokens = regextokenzr.tokenize(raw)
text = nltk.Text(tokens)

# NORMALIZE WORDS - PART 1
stop_words = set(stopwords.words('english')+["a", "the"])
words = [w.lower() for w in text]

# NORMALIZE WORDS - PART 2
#words = [w.lower() for w in text if w.lower() not in stop_words]

# BIGRAM DATA
bigrams = bigrams(words)
bigrams = list(bigrams)
bigrams_counter = Counter(bigrams)
print(len(sorted(bigrams_counter)))

pairs = [tup for tup in bigrams if not False in [False for wrd in tup if wrd in stop_words] ]

pairs_counter = Counter(pairs)
print(pairs_counter.most_common(15))
print(len(sorted(pairs_counter)))

# BUILD VOCABULARY
#vocab = Counter(words)
#print (vocab.most_common(5))


# NORMALIZE TEXT: TOKENIZE AND THEN DETERMINE BEGINNING

