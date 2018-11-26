import os
from _helper import simple_get, json_helper
from bs4 import BeautifulSoup
import difflib

pokemon_list = open('../pokemonList/pokemonlist.txt', 'r')

f = open("pokemon.json", "a")

f.write("{\n")

list = pokemon_list.readlines()
base_url = 'https://bulbapedia.bulbagarden.net'
url = str(base_url+ list[0].strip())

raw_html = simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')
## Stat Table
stat_table_number = 128
name_pokemon = html.select('h1#firstHeading')[0].text.split(' ', 1)[0]

f.write(json_helper(0))
f.write("\t")
f.write(json_helper("name", name_pokemon)+ ", \n")
f.write("\t")
table = html.select('table')[stat_table_number]
tr = table.select('table')
f.write(json_helper("stats"))

for value in range(0, 6):
  name = tr[value].select('th')[0].select('a')[0].text.rstrip()
  value = tr[value].select('th')[1].text.rstrip()
  f.write("\t\t")
  f.write(json_helper(name, value.strip())+", \n")

f.write("\t\t}\n")
f.write("\t}")
f.write("\n}")