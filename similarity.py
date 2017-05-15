''' Text Similarity

		General Work-flow:
			1. Text Normalization
			2. Vectorization - TF-IDF
			3. Cosine Similarity

'''

#TODO: IMPLEMENT FUNCTION TO RETURN MOST SIMILAR DOC BASED ON COMPUTATIONS AGAINST A SPECIFIC DOC

import pandas as pd
from scipy.spatial.distance import cosine


file = 'results/simple-tf-idf.csv'
matrix = pd.DataFrame.from_csv(file, header=0)

dracula = matrix.loc[345, :]
bovary = matrix.loc[2413, :]

print(cosine(dracula, bovary))

# file = 'results/nolan-tf-idf.csv'
# matrix = pd.DataFrame.from_csv(file, header=0)

# following = matrix.loc['following-dialogue.txt', :]
# memento = matrix.loc['memento.txt', :]
# insomnia = matrix.loc['insomnia.txt', :]
# prestige = matrix.loc['the-prestige.txt', :]
# inception = matrix.loc['inception.txt', :]
# begins = matrix.loc['batman-begins.txt', :]
# tdk = matrix.loc['the-dark-knight.txt', :]
# tdkr = matrix.loc['the-dark-knight-rises.txt', :]
# intersteller = matrix.loc['intersteller.txt', :]

# print(1 - cosine(following, begins))
# print(1 - cosine(following, tdk))
# print(1 - cosine(following, tdkr))

# print(1 - cosine(following, intersteller))
# print(1 - cosine(following, inception))
# print(1 - cosine(following, prestige))
# print(1 - cosine(following, insomnia))