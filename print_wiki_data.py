import requests
from bs4 import BeautifulSoup
from print_shtml import print_shtml

def get_html(url):
	resp = requests.get(url,headers ={'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
	return resp.text

def clean_ele(e):
	for c in e.find_all('div',class_='shortdescription'):
		c.decompose()
	for c in e.find_all('table',class_='infobox'):
		c.decompose()
	for c in e.find_all('style'):
		c.decompose()
	for c in e.find_all('meta'):
		c.decompose()
	for c in e.find_all('figure'):
		c.decompose()

def clean_p(p):
	for c in p.find_all('sup'):
		c.decompose()
	for c in p.find_all('a'):
		c.unwrap()

def print(url):
	text   = get_html(url)
	doc = BeautifulSoup(text,'html5lib')
	f = doc.find_all('div',class_='mw-content-ltr')[0]
	clean_ele(f)
	shtml = ['<html>']
	for c in f.children :
		if c.name == 'p':
			clean_p(c)
			shtml.append('<p>'+c.text+'</p>')
		elif c.name == 'h2':
			span = c.find_all('span',class_='mw-headline')[0]
			t = span.text.strip()
			if t == 'Footnotes' or t == 'Reference':
				break
			shtml.append('<h>'+t+'</h>')
	shtml.append('</html>')
	print_shtml(' '.join(shtml))

