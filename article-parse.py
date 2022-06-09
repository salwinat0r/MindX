from newspaper import Article
import nltk
nltk.download('stopwords')

def getTags(url):
    # parsing the article
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    
    # remove plurals
    tags = list(article.keywords)
    for i in range(len(tags)):
        if tags[i][-1] in tags:
            tags[i] = tags[i][:-1]
    tags = list(set(tags))
    
    #remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    tags = [tag for tag in tags if tag not in stop_words]
    return tags

url = input("Enter article URL: ")
print(getTags(url))