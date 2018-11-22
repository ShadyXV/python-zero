from _helper import simple_get
from bs4 import BeautifulSoup
import sys
import json

repoName = []
repoLink = []



def populateData(url):
  raw_html = simple_get(url)
  html = BeautifulSoup(raw_html, 'html.parser')
  repos = html.find_all("a", {"itemprop": "name codeRepository"})

  for repo in repos:
    repoName.append(repo.text)
    repoLink.append('http://github.com' + repo["href"])

  pagination = html.find_all("div", {"class": "pagination"})
  next = html.find_all("a", {"rel": "nofollow"})

  nextUrl = None

  if len(pagination) == 1 :
    if next[1].text == 'Next' :
      nextUrl = next[1]["href"]

  return nextUrl

try:
  userName= sys.argv[1]
  url = "http://github.com/"+userName+"?tab=repositories"
  while True:
    nextUrl = populateData(url)
    if nextUrl == None:
      break
    else:
      url = nextUrl

except Exception:
  print ('Command : python main.py <gitHub username>')


for i in range(0, len(repoName)) :
  print(repoName[i])
  print(repoLink[i])
