'''
@author: Will

Description: clean twitter data and identify tweets related to White House
             leaks
'''

import pandas as pd
import numpy as np
import re

root = r'/project/rcc/deep_learning_hack/dc-taxi/DCTaxiCab/'

handles = {
    'cnnbrk': 'CNN Breaking News',
    'jonathanvswan': 'Jonathan Swan',
    'maggieNYT': 'Maggie Haberman',
    'washingtonpost': 'Washington Post',
    'politico': 'Politico',
    'msnbc': 'MSNBC',
    'FoxNews': 'Fox News',
    'WSJ': 'Wall Street Journal',
    'nytimes': 'New York Times',
    'HuffPostPol': 'Huffington Post',
    'CNNPolitics': 'CNN Politics',
    'axios': 'AXIOS',
    'CBSPolitics': 'CBS Politics',
    'CillizzaCNN': 'Chris Cillizza',
    'NBCPolitics': 'NBC Politics',
    'AP': 'Associated Press',
    'Reuters': 'Reuters',
    'BBCBreaking': 'BBC Breaking News',
    'thehill': 'The Hill'
}

tweets = pd.DataFrame()

for handle in handles.keys():
    try:
        df = pd.read_csv(root + '/data/twitter/raw/' + handle + '.csv',
                         encoding='latin1')
        df['tweet_source'] = handles[handle]
        tweets = pd.concat([df, tweets])
    except:
        pass

tweets.text = tweets.text.str.lower()

word_list = [
    'trump', 'white house', 'washington', 'washington post', 'kushner',
    'flynn', 'conway', 'source', 'leak', 'preibus', 'congress', 'russia',
    'emails', 'hack', 'spicer', 'elliott', 'abrams', 'tillerson', 'secretary'
]

for word in word_list:
    tweets[word] = tweets.text.str.contains(word)

tweets.to_csv(root + '/data/twitter/intermediate/tweets.csv')

