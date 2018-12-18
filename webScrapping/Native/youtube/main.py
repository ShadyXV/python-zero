import requests
import re

def ytsearch(num, query):
    html = requests.get("https://youtube.com/results?search_query={}".format(query))
    html = str(html.content)
    dresults = (re.findall('href=\"/watch\?v=(.{11})', html))
    results = []
    for result in dresults:
        if result in results:
            continue
        else:
            results.append(result)
    if num > len(results):
        num = len(results)
    for x in range(num):
        link = "https://youtu.be/" + results[x]
        print(link)

query = input("search query\n")
num = input("how many link  do you want ?\n")

try:
    num = int(num)
except Exception:
    num = 1

ytsearch(num, query)