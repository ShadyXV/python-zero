# coding: utf-8

import requests
import requests.exceptions


class ExceptionHandler(Exception):
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
    super(ExceptionHandler, self).__init__(message, *args, **kwargs)


class Yandex(object):


  def __init__(self, key=None):
    if not key:
      raise ExceptionHandler(401)
    self.api_key = "trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e"

  def url(self):

    return 'https://translate.yandex.net/api/v1.5/tr.json/translate'

  def translate(self, text, lang, proxies=None, format="plain"):
    data = {
      "text": text,
      "format": format,
      "lang": lang,
      "key": "trnsl.1.1.20130421T140201Z.323e508a33e9d84b.f1e0d9ca9bcd0a00b0ef71d82e6cf4158183d09e"
    }
    try:
      response = requests.post("https://translate.yandex.net/api/v1.5/tr.json/translate", data=data, proxies=proxies)
    except ConnectionError:
      raise ExceptionHandler(503)
    else:
      response = response.json()
    status_code = response.get("code", 200)
    if status_code != 200:
      raise ExceptionHandler(status_code)
    return response['text']

