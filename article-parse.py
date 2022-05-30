from newspaper import Article
import nltk

def getTags(url):
    article = Article(url)
    article.download()
    article.parse()
    article.nlp()
    tags = list(article.keywords)
    for i in range(len(tags)):
        if tags[i][-1] in tags:
            tags[i] = tags[i][:-1]
    tags = list(set(tags))
    return tags

url = input("Enter article URL: ")
getTags(url)
