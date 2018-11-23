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
print(raw_html)
