from _helper import simple_get
from bs4 import BeautifulSoup
import requests




def getUrl(frm, to , text):
  return "https://translate.google.com/#view=home&op=translate&sl={}&tl={}&text={}".format(frm, to, text)


# Set up the parameters we want to pass to the API.
# This is the latitude and longitude of New York City.
data = {
  "text": "text",
  "format": "plain",
  "lang": "ru",
  "key": "trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e"
}

# Make a get request with the parameters.
response = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate", data=data, proxies=None)

# Print the content of the response (the data the server returned)
print(response.content)

# This gets the same data as the command above
# response = requests.get("http://api.open-notify.org/iss-pass.json?lat=40.71&lon=-74")
# print(response.content)
