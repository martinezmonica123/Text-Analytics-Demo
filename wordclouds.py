from os import path
from urllib import urlopen
import random

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from freq_gutenberg import STOP_WORDS, get_data


STOP_WORDS.add("said")


def create_wordcloud(raw_data, title, bigrams=True):
	''' Generate Word Cloud -- Word_Cloud Library: https://github.com/amueller/word_cloud '''

	# Black to Grey
	def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
	    return "hsl(0, 0%%, %d%%)" % random.randint(10, 60)
	    
	d = path.dirname(__file__)

	wordcloud = WordCloud(font_path=path.join(d, "fonts/raleway/raleway-light.ttf"), width=500, height=500, margin=20, background_color='white', max_words=20,
	               stopwords=STOP_WORDS, color_func=custom_color_func, random_state=20)
	
	wordcloud.collocations = bigrams
	wordcloud.generate(raw_data)

	plt.imshow(wordcloud)
	wordcloud.to_file("word_clouds/" + title + ".png")
	print ('Created Word Cloud')


if __name__ == '__main__':

	# mobydick = get_data("https://www.gutenberg.org/files/2701/2701-0.txt", 6529, 1242147)
	# create_wordcloud(mobydick, 'Moby_Dick')

	# madamebovary = get_data("https://www.gutenberg.org/files/2413/2413-0.txt", 1443, 666170)
	# create_wordcloud(madamebovary, 'Madame_Bovary')

	# dracula = get_data("https://www.gutenberg.org/cache/epub/345/pg345.txt", 4173, 863843)
	# create_wordcloud(dracula, 'Dracula')

	# huckfinn = get_data("https://www.gutenberg.org/files/76/76-0.txt", 9804, 587674)
	# create_wordcloud(huckfinn, 'Huck_Finn')

	# frankenstein = get_data("https://www.gutenberg.org/cache/epub/84/pg84.txt", 798, 429467)
	# create_wordcloud(frankenstein, 'Frankenstein')

	# metamorphosis = get_data("https://www.gutenberg.org/cache/epub/5200/pg5200.txt", 871, 122000)
	# create_wordcloud(metamorphosis, 'Metamorphosis')

	# emma = get_data("https://www.gutenberg.org/files/158/158-0.txt", 667, 899917) 
	# create_wordcloud(emma, 'Emma')
