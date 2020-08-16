'''
Jeremy Thaller
August 2nd, 2020

This script opens the pickle made from the preprocessing.py script. 
Then creates a word cloud and saves it as a jpg. You might need to add a few
stop words to get a better result.
'''

import numpy as np
import pandas as pd
from os import path
# from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

# %matplotlib inline
import matplotlib.pyplot as plt


df = pd.read_pickle('sarah_cleaned_messages_df.pickle')


# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    fig = plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")
    plt.show()
    fig.savefig("sarah_cloud.png")


# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='blue',
colormap='Set2', collocations=False, stopwords = ['lol', 'ok', 'good', 'lolol', 're'] + list(STOPWORDS)).generate(' '.join(df['content']))
                    #   colormap='Set2', collocations=False, stopwords = ['bc','didn','bu','lol', 'ok', 'good', 'lolol', 'don', 't', 'll','nt', 've'] + list(STOPWORDS)).generate(' '.join(df['content']))

# Plot
plot_cloud(wordcloud)


