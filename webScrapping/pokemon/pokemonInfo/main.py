import os
from _helper import simple_get
from bs4 import BeautifulSoup

pokemon_list = open('../pokemonList/pokemonlist.txt', 'r')

# print(len(contents))
# for line in contents:
#   print(line)
list = pokemon_list.readlines()
url = list[0]
print(url)
raw_html = simple_get('https://bulbapedia.bulbagarden.net/wiki/Bulbasaur_(Pok%C3%A9mon)')
# html = BeautifulSoup(raw_html, 'html.parser')
# print(raw_html)

