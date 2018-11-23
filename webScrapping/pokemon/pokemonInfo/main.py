import os
from _helper import simple_get
from bs4 import BeautifulSoup
import difflib

pokemon_list = open('../pokemonList/pokemonlist.txt', 'r')



list = pokemon_list.readlines()
base_url = 'https://bulbapedia.bulbagarden.net'
url = str(base_url+ list[0].strip())

raw_html = simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')
## Stat Table
stat_table_number = 128
table = html.select('table')[stat_table_number]
tr = table.select('table')
for value in range(0, 6):
  name = tr[value].select('th')[0].select('a')[0].text
  value = tr[value].select('th')[1].text
  print(value)
