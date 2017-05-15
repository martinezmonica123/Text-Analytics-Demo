from os import listdir, path
from urllib import urlopen
import csv
import sys

import requests
from bs4 import BeautifulSoup


csv.field_size_limit(sys.maxsize)
reload(sys)
sys.setdefaultencoding('utf-8')


def read_textfile(filename):
	''' Read the contents of FILENAME and return as string'''
	infile = open(filename)
	contents = infile.read()
	infile.close()
	return contents


def read_csvfile(filename):
	dict_list = []
	
	reader = csv.DictReader(open(filename, 'rb'))
	for row in reader:
		dict_list.append(row)
	return dict_list


# website: www.imsdb.com
def get_website_data(url):
	page = requests.get(url)
	soup = BeautifulSoup(page.content, 'html.parser')
	#script = soup.find("td", {"class": "scrtext"})
	return soup


#TODO: UPDATE DESCRIPTION
def get_gutenberg_data(dict_list):
	for d in dict_list:
		url = d['url']
		start = int(d['start_index'])
		end = int(d['end_index'])

		raw = urlopen(url).read().decode('utf8')
		raw = raw[start:end]
		
		d['raw_text'] = raw
	return dict_list


def to_csvfile(dict_data, filename):
	keys = dict_data[0].keys()
	with open(filename, 'wb') as output_file:
	    dict_writer = csv.DictWriter(output_file, keys)
	    dict_writer.writeheader()
	    dict_writer.writerows(dict_data)
	print('Finished writing to csv')


def list_textfiles(directory):
	''' Return a list of filenames ending in '.txt' in DIRECTORY'''
	textfiles = []
	for filename in listdir(directory):
		if filename.endswith(".txt"):
			textfiles.append(filename)
	return textfiles
