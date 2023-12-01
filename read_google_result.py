from bs4 import BeautifulSoup

from urllib.parse import urlparse


def get_domain(input):
    try:
        return urlparse(input).netloc
    except:
        return None

def read_result(html):
    result=[]
    doc = BeautifulSoup(html,'html.parser')
    f = doc.find_all('a')
    for a1 in f:
        h3 = a1.find('h3')
        domain = get_domain(a1.get('href'))
        if h3 and domain:
            result.append({'a' : a1.get('href'),'txt' : h3.text ,'dom' : domain})
    return result
        
