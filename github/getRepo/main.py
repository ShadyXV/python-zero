from _helper import simple_get
from bs4 import BeautifulSoup
import sys

try:
  userName= sys.argv[1]
  url = "http://github.com/"+userName+"?tab=repositories"
  raw_html = simple_get(url)
  html = BeautifulSoup(raw_html, 'html.parser')
  div = html.select("div#user-repositories-list")
  anotherDiv = BeautifulSoup(div, "html.parser")

except Exception:
  print ('Error')

# check if the