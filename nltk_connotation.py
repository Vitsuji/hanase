import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import csv

para = input("")

sentence = word_tokenize(para)

word_features = []

for word, position in nltk.pos_tag(sentence):
    if position in ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS', 'VBP', 'VBG', 'VBD', 'VBN' 'VBG', 'NN']: 
        word_features.append(word)


rating = 0

for word in word_features:
    with open('words.txt', 'rt') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            list_conn = row[1].split()
            for connotation in list_conn:
                if word == connotation:
                    if row[0] == 'pos':
                        print("pos+")
                        rating = rating + 1
                    elif row[0] == 'neg':
                        print("neg-")
                        rating = rating - 1
print(rating)


