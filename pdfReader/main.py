import PyPDF2
# import textract

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import json
import os

filename = 'booklet.pdf'
#open allows you to read the file
pdfFileObj = open(filename,'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages

count = 0
text = ''
allWords = []

while count < num_pages - 1:
  pageObj = pdfReader.getPage(count)
  count+= 1
  filterText = pageObj.extractText().replace('\n', '')
  filterText = filterText.replace('G L U E','')
  filterText = filterText.replace('  ', '\n')
  allText = filterText.split('\n')

  for text in allText:
    if len(text) > 2 :
      if len(allWords) < 26:
        allWords.append(text)

f = open("pdfResource.txt", "a")
for values in allWords:
  f.write(values +"\n")