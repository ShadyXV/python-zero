# url https://pokemondb.net/move/generation/1

import os
from __helper import simple_get, json_helper
from bs4 import BeautifulSoup

field_names = ["attack_name", "type", "category", "power", "accuracy", "power_points", "description"]

## open the file to write
f = open("pokemon.json", "w")


url = 'https://pokemondb.net/move/generation/1'
raw_html = simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')

def run():
  f.write("{\n")
  required_table = html.select('table')[0]
  rows = required_table.select('tr')
  index = 0
  for row in rows:
    columns = row.select("td")
    if index :
      f.write('\t' + json_helper(index))
    for i in range(0, len(columns)):
      if i == 1:
        attackType = columns[i].select('a')[0].text
        f.write('\t\t'+ json_helper(field_names[i], attackType) + ", \n")
      elif i == 2 :
        category = columns[i].select('span')[0].attrs['title']
        f.write('\t\t'+ json_helper(field_names[i], category) + ", \n")
      else:
        f.write('\t\t'+ json_helper(field_names[i], columns[i].text) + ", \n")
        pass
    if index:
      f.write("\t },\n")
    index += 1
  f.write("}")

run()