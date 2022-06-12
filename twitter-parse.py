from re import T
import tweepy
import nltk
from nltk import word_tokenize, pos_tag, pos_tag_sents
from dotenv import load_dotenv, find_dotenv
import os
load_dotenv(find_dotenv())

consumer_key = os.environ.get('CONSUM_KEY')
consumer_secret = os.environ.get('CONSUM_SECR')
access_token = os.environ.get('ACC_TOK')
access_token_secret = os.environ.get('ACC_TOK_SEC')



def TwitterParse(id):
    # set access to user's access key and access secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    status = api.get_status(id, tweet_mode = 'extended')

    # check for meadia in the tweet
    if 'media' in status.entities:
        for image in  status.entities['media']:
            print(image['media_url'])
    
    # fetching the text attribute
    text = status.full_text
    tokens = set(word_tokenize(text))
    tokens = pos_tag(tokens)
    # check for nouns in the token list
    tagged_tok=[]
    for i in range(len(tokens)):
        if tokens[i][1]=="NNP" or tokens[i][1]=="NNS" or tokens[i][1]=="NN":
            tagged_tok.append(tokens[i][0])
    
    # remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tagged_tok if word not in stop_words]
    return tagged_tok

id= '1535569677971345409'
print(TwitterParse(id))