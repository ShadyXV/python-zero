from __helper import simple_get, json_helper
from bs4 import BeautifulSoup
import json
import os

first_gen_type = []
first_gen_type_color = []

first_gen_url = 'https://bulbapedia.bulbagarden.net/wiki/Type'


raw_html = simple_get(first_gen_url)
check_web = len(raw_html) > 0
html = BeautifulSoup(raw_html, 'html.parser')

if (check_web) :
  table = html.select('table')[0]
  tr_len = len(table.select('tr'))
  for i in range(2, tr_len - 2) :
    row=  table.select('tr')[i]
    column = row.select("td")
    if(column[0]):
      first_gen_type.append(column[0].text)
      first_gen_type_color.append(column[0]["style"].split(';')[6].split(':')[1])
    if (column[1]) :
      first_gen_type.append(column[1].text)
      first_gen_type_color.append(column[1]["style"].split(';')[6].split(':')[1])

f = open("pokemon.json", "w")

f.write("{\n")

for i in range(0, len(first_gen_type)):
  f.write('\t'+ json_helper(first_gen_type[i].strip('\n'), first_gen_type_color[i]+ ",\n"))
  f.write(",\n")
f.write("}")
f.close()


