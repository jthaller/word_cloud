import numpy as np
import pandas as pd
from os import path
# from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
% matplotlib inline

df = pd.read_pickle('sarah_cleaned_messages_df.pickle')
print(df.head())

# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    fig = plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off")
    plt.show()
    fig.savefig("ZJ_cloud.png")


# Generate wordcloud
wordcloud = WordCloud(width = 3000, height = 2000, random_state=1, background_color='pink', 
                      colormap='Set2', collocations=False, stopwords = ['lol', 'ok', 'good', 'lolol'] + list(STOPWORDS)).generate(' '.join(df['content']))
# Plot
plot_cloud(wordcloud)