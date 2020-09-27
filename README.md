# word_cloud
I built some word clouds based off of my facebook messenger data

The project takes my facebook chat data (stored as a JSON) and creates a word cloud for a chosen friend. ```preprocessing.py``` reads in the JSON and then adds the data into a pandas dataframe. It then cleans the text by fixing the decoding mode, removing url's, and consolidating common words that are frequently spelled differently (e.g. heyyy and heyyyy get counted as one word). It then saves the DF as a pickle file. ```make_cloud.py``` is actually pretty simple. It just grabs the pre-processed dataframe pickle, then creates a word cloud and saves the image.

![](https://github.com/jthaller/word_cloud/blob/master/sarah_cloud.png)

## What's next
I'm not thrilled with this implimentation because the clouds for my friends are all pretty similar. That shouldn't be surprising, though. I wrote it so that it's basically just finding the most common words that aren't included in the STOPWORDS list. It would be better to give it a full corpus of and then do TF-IDF for each friend's chat in order to find the most important words for each friend.
