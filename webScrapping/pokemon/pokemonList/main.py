from __helper import simple_get
from bs4 import BeautifulSoup
import json
import os

first_gen_list_pokemon = []

raw_html = simple_get('https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_Kanto_Pok%C3%A9dex_number')
check_web = len(raw_html) > 0
html = BeautifulSoup(raw_html, 'html.parser')
if (check_web) :
  for k in range(1, 4):
    table = html.select('table')[k]
    tr_len = len(table.select('tr'))
    for i in range(1, tr_len) :
      tr=  table.select('tr')[i]
      a = tr.select('a')[1]
      first_gen_list_pokemon.append(a['href'])


# print(json.dumps(first_gen_list_pokemon))
f = open("pokemonlist.txt", "a")
f.write(json.dumps(first_gen_list_pokemon))