from newspaper import Article

url = input("")
article = Article(url)
article.download()
article.parse()
article.nlp()

tags = list(article.keywords)
print(tags[5])