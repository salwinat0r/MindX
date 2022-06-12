from re import T
import tweepy
import nltk
from nltk import word_tokenize, pos_tag_sents

consumer_key = 'jUXANq60QoEbLzt1YRiQeUVaO'
consumer_secret = 'aPvmdRkI1sA0BEonChYHj5KoSoamlryPWdDiR4kqhNlVflA8Pu'
access_token = '4662587646-MlfQI4uZBlV0hI8ge2wEupXCSWueyvwkd9uCiyr'
access_token_secret = 'fAZFKy0snAeGn3zYAbsOcIxfTdI2YGnUQXah6cxdhr5e0'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# set access to user's access key and access secret 
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

id= '1535569677971345409'

status = api.get_status(id, tweet_mode = 'extended')

# if image exists in the tweet
if 'media' in status.entities:
    for image in  status.entities['media']:
        print(image['media_url'])

# fetching the text attribute
text = status.full_text
tokens = set(word_tokenize(text))
tokens = nltk.pos_tag_sents(tokens)
tagged_tok=[]
for i in range(len(tokens)):
  if tokens[i][1]=="NNP" or tokens[i][1]=="NNS" or tokens[i][1]=="NN":
    tagged_tok.append(tokens[i][0])

def removeStopWords(tagged_tok):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tokens = [word for word in tagged_tok if word not in stop_words]
    return tagged_tok

print(removeStopWords(tagged_tok))