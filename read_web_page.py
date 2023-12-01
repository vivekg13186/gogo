from newspaper import Article

def read_page(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text
