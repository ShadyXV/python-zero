from mathematicians import simple_get
from bs4 import BeautifulSoup

raw_html = simple_get('https://realpython.com/blog/')
print(len(raw_html))

raw_html = simple_get('http://www.fabpedigree.com/james/mathmen.htm')
html = BeautifulSoup(raw_html, 'html.parser')
for i, li in enumerate(html.select('li')):
  print(i, li.text)