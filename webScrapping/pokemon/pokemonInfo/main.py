import os
from _helper import simple_get, json_helper
from bs4 import BeautifulSoup


## open the file to write


f = open("pokemon.json", "a")

f.write("{\n")


url = 'https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_base_stats_(Generation_I)'
raw_html = simple_get(url)
html = BeautifulSoup(raw_html, 'html.parser')

required_table = html.select('table')[0]
rows = required_table.select('tr')
for individual in range(1, len(rows)):
  f.write('\t' + json_helper(individual))
  row = rows[individual]
  column = row.select("td")
  evolutionid = individual + 1
  f.write('\t\t'+ json_helper('Name', column[2].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('HP', column[3].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('Attack', column[4].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('Defense', column[5].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('Speed', column[6].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('Special', column[7].text.strip()) + ", \n")
  f.write('\t\t'+ json_helper('Level', '15') + ", \n")
  f.write('\t\t'+ json_helper('EvolutionId', str(evolutionid)) + ", \n")
  f.write('\t\t'+ json_helper('Type', "[]") + ", \n")
  f.write("\t },\n")


f.write("}")
f.close()