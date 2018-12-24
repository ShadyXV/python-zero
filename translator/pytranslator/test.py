# coding: utf-8

import requests
import requests.exceptions


class YandexTranslateException(Exception):
  """
  Default YandexTranslate exception
  """
  error_codes = {
    401: "ERR_KEY_INVALID",
    402: "ERR_KEY_BLOCKED",
    403: "ERR_DAILY_REQ_LIMIT_EXCEEDED",
    404: "ERR_DAILY_CHAR_LIMIT_EXCEEDED",
    413: "ERR_TEXT_TOO_LONG",
    422: "ERR_UNPROCESSABLE_TEXT",
    501: "ERR_LANG_NOT_SUPPORTED",
    503: "ERR_SERVICE_NOT_AVAIBLE",
  }

  def __init__(self, status_code, *args, **kwargs):
    message = self.error_codes.get(status_code)
    super(YandexTranslateException, self).__init__(message, *args, **kwargs)


class YandexTranslate(object):

  api_url = "https://translate.yandex.net/api/v1.5//tr.json/translate"

  def __init__(self, key=None):
    if not key:
      raise YandexTranslateException(401)
    self.api_key = "trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e"

  def url(self):

    return 'https://translate.yandex.net/api/v1.5/tr.json/translate'

  @property
  def directions(self, proxies=None):

    try:
      response = requests.get(self.url("langs"), params={"key": self.api_key}, proxies=proxies)
    except requests.exceptions.ConnectionError:
      raise YandexTranslateException(self.error_codes[503])
    else:
      response = response.json()
    status_code = response.get("code", 200)
    if status_code != 200:
      raise YandexTranslateException(status_code)
    return response.get("dirs")

  @property
  def langs(self):
    """
    Returns list with supported languages
    >>> translate = YandexTranslate("trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e")
    >>> languages = translate.langs
    >>> len(languages) > 0
    True
    """
    return set(x.split("-")[0] for x in self.directions)

  def detect(self, text, proxies=None, format="plain"):
    data = {
      "text": text,
      "format": format,
      "key": self.api_key,
    }
    try:
      response = requests.post(self.url("detect"), data=data, proxies=proxies)
    except ConnectionError:
      raise YandexTranslateException(self.error_codes[503])
    except ValueError:
      raise YandexTranslateException(response)
    else:
      response = response.json()
    language = response.get("lang", None)
    status_code = response.get("code", 200)
    if status_code != 200:
      raise YandexTranslateException(status_code)
    elif not language:
      raise YandexTranslateException(501)
    return language

  def translate(self, text, lang, proxies=None, format="plain"):
    data = {
      "text": text,
      "format": format,
      "lang": lang,
      "key": "trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e"
    }
    try:
      response = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate", data=data, proxies=proxies)
      print(response.url, response)
    except ConnectionError:
      raise YandexTranslateException(503)
    else:
      response = response.json()
    status_code = response.get("code", 200)
    if status_code != 200:
      raise YandexTranslateException(status_code)
    return response



translate = YandexTranslate
result = translate.translate(translate, lang="ru", text="Hello, world!")
print(result)
