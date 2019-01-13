
# coding: utf-8

# ### Goal
# The goal of this repo is show the analyze the positive and negative words used in a corpora following sentiment analysis rules. The user will be able to see how the choice of words affect the overall message the author is trying to convey. The choice of positive and negative words can affect the meaning of the text. 
# 
# ### Part 1
# 
# Write a function that generates a simple sentiment analysis of all the corpora in the inputted directory. The sentiment_analysis method takes in a string positive text file, negative text file, corpora path, and return the analysis in a list of objects:
#     eg: [{'1 King Henry Iv': {'positive': 929, 'neutral': 989, 'overall': 'negative', 'negative': 989}}]
# 
# ### Part 2
# Write a function that generates a scatter plot of the positive count and negative count words in all of the corpora. The function should input the analysis_dict generated in part 1
# 
# ### Part 3
# Write a function that creates a word cloud displaying positive and negative words used in a selected text file. There should be seperate word clouds for positive and negative words. The final combined word cloud should show the relationship of positive/negative words and provide brief details about the inputted file. 
#     Note: be sure to install the wordcloud package
#     !conda install --yes -c conda-forge wordcloud 
# 

# In[ ]:

get_ipython().magic(u'matplotlib inline')

# Imports
import glob
import operator
import os
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# In[ ]:

# Functions for processing text
def tokenize(s, tokenize_char=None):
    """
    The tokenize method removes non-word strings

    :param str s: list of strings
    :return: string of text
    :rtype: str
    """
    punctuations = "-,.?!;: \n\t"
    s = [t.strip(punctuations) for t in s.split(tokenize_char)]
    s = [t for t in s if t != '']
    return s

def preprocess(s, case = "L"):
    """
    The preprocess method preprocess file

    :param str s: list
    :return: list of words
    :rtype: str
    """
    if case == "L":
        s = s.lower()
    elif case == "U":
        s = s.upper()
    return s


def title_strip(s):
    """
    The title_strip method takes in a string title, split,
    and return the title in string format

    :param str s: directory of title
    :return: string of title
    :rtype: str
    """
    s = os.path.split(s)[1][:-4].replace("_", " ").title()
    return s


# In[ ]:

def sentiment_analysis(pos_words_txt, neg_words_txt, corpora_path):
    """
    The sentiment_analysis method takes in a string positive text file, 
    negative text file, corpora path, and return the analysis in string format
    eg: [{'1 King Henry Iv': {'positive': 929, 'neutral': 989, 'overall': 'negative', 'negative': 989}}]

    :param str pos_words_txt: directory of positive
    :param str neg_words_txt: directory of negative
    :param str corpora_path: directory of path
    :return: list of objects
    :rtype: str
    """
    
    filenames = glob.glob(corpora_path)
    analysis_dict = []
    
    # Gather list of positive and negative words
    positive_words = [pword.rstrip() for pword in open(pos_words_txt, 'r').readlines()[35:]]
    negative_words = [nword.rstrip() for nword in open(neg_words_txt, 'r').readlines()[35:]]

    for fn in filenames:
        pos_words = 0
        neg_words = 0
        neu_words = 0
        overall = ""
        title = title_strip(fn)

        # open file
        words = open(fn, 'r').read()
        # preprocess
        words = preprocess(words)
        # tokenize
        words = tokenize(words) 

        for w in words:
            if w in positive_words:
                pos_words += 1
            elif w in negative_words:
                neg_words += 1
            else:
                neu_words += 1
        if pos_words > neg_words:
            overall = "positive"
        elif pos_words < neg_words:
            overall = "negative"
        else:
            overall = "neutral"

        analysis_dict.append({title: {"positive": pos_words, "negative": neg_words, "neutral": neu_words, "overall": overall}})
    return analysis_dict


# In[ ]:

# Run the sentiment analysis on shakespeare corpora 
analysis_dict = sentiment_analysis('positive-words.txt', 'negative-words.txt', '../corpora/shakespeare_plaintext/*.txt')   


# In[ ]:

def create_scatter(analysis_dict):
    """
    The create_scatter method takes in the analysis dict and outputs a scatter plot
    of the positive count and negative count words in all of the corpora

    :param list of objects analysis_dict: list of objects
    :return: scatter plot
    :rtype: plot
    """
    positive = []
    negative = []
    labels = []
    for a in analysis_dict:
        key = a.keys()[0]
        positive.append(a[key]['positive'])
        negative.append(a[key]['negative'])
        labels.append(key)
    
    plt.figure(figsize=(15,12))
    plt.xlabel("positive count")
    plt.ylabel("negative count")
    plt.scatter(positive, negative, s=200, alpha=.5)
    for i, l in enumerate(labels):
        plt.text(positive[i], negative[i], l)


create_scatter(analysis_dict)


# In[ ]:

# install word cloud
get_ipython().system(u'conda install --yes -c conda-forge wordcloud ')


# In[ ]:

# Gather list of positive and negative words
# MAKING GLOBAL
positive_words = [pword.rstrip() for pword in open('positive-words.txt', 'r').readlines()[35:]]
negative_words = [nword.rstrip() for nword in open('negative-words.txt', 'r').readlines()[35:]]


# In[ ]:

def create_art(fn):
    pos_text = ""
    neg_text = ""

    # open file
    words = open(fn, 'r').read()
    # preprocess
    words = preprocess(words)
    # tokenize
    words = tokenize(words) 
    
    # Gather text of positive and negative words
    for w in words:
        if w in positive_words:
            pos_text += " " + w
        elif w in negative_words:
            neg_text += " " + w

    # Generate a word cloud image
    wordcloud = WordCloud().generate(pos_text)

    # Display the generated image for positive words:    
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title("Positive Words")
    plt.axis("off")
    
    # Display the generated image for negative words:    
    wordcloud = WordCloud().generate(neg_text)
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title("Negative Words")
    plt.axis("off")
    
    # output
    plt.show()
    
create_art('../corpora/shakespeare_plaintext/hamlet.txt')


# In[ ]:

from wordcloud import (WordCloud, get_single_color_func)
import matplotlib.pyplot as plt


class SimpleGroupedColorFunc(object):
    """Create a color function object which assigns EXACT colors
       to certain words based on the color to words mapping
       Parameters
       ----------
       color_to_words : dict(str -> list(str))
         A dictionary that maps a color to the list of words.
       default_color : str
         Color that will be assigned to a word that's not a member
         of any value from color_to_words.
    """

    def __init__(self, color_to_words, default_color):
        self.word_to_color = {word: color
                              for (color, words) in color_to_words.items()
                              for word in words}

        self.default_color = default_color

    def __call__(self, word, **kwargs):
        return self.word_to_color.get(word, self.default_color)

def plot_title(f, analysis_dict):
    for a in analysis_dict:
        if f in a:
            title_dict = a
    return f + "\n overall rating: " + title_dict[title]['overall'] + "\n # of positive words: " + str(title_dict[title]['positive']) + "\n # of negative words: " + str(title_dict[title]['negative'])

# get plot title
title = title_strip('../corpora/shakespeare_plaintext/hamlet.txt')
title = plot_title(title, analysis_dict)
# open file
words = open('../corpora/shakespeare_plaintext/hamlet.txt', 'r').read()
# preprocess
words = preprocess(words)
# tokenize
words = tokenize(words)

text = ""
# Gather text of positive and negative words
for w in words:
    if w in positive_words or w in negative_words:
        text += " " + w

wc = WordCloud(collocations=False).generate(text)

color_to_words = {
    'green': positive_words,
    'red': negative_words
}

default_color = 'grey'

# Create a color function with single tone
grouped_color_func = SimpleGroupedColorFunc(color_to_words, default_color)

# Apply our color function
wc.recolor(color_func=grouped_color_func)

# Plot
plt.figure()
plt.imshow(wc, interpolation="bilinear")
plt.title(title)
plt.axis("off")
plt.show()

