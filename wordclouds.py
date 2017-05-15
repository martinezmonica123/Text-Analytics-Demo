from os import path
from urllib import urlopen
import random

from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from normalization import STOP_WORDS
from data_scraping import read_textfile


STOP_WORDS.add("said")


def create_wordcloud(raw_data, title, bigrams=True):
	''' Generate Word Cloud -- Word_Cloud Library: https://github.com/amueller/word_cloud '''

	# Black to Grey
	def custom_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
	    return "hsl(0, 0%%, %d%%)" % random.randint(10, 60)
	    
	d = path.dirname(__file__)

	wordcloud = WordCloud(font_path=path.join(d, "fonts/raleway/raleway-light.ttf"), width=500, height=500, margin=20, background_color='white', max_words=30,
	               stopwords=STOP_WORDS, color_func=custom_color_func, random_state=20)
	
	wordcloud.collocations = bigrams
	wordcloud.generate(raw_data)

	plt.imshow(wordcloud)
	wordcloud.to_file("word_clouds/" + title + ".png")
	print ('Created Word Cloud')


if __name__ == '__main__':
	# d = path.dirname(__file__)

	# memento = read_textfile(path.join(d, "data/memento.txt"))
	# create_wordcloud(memento, 'Memento')
