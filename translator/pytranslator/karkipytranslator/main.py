from yandex import Yandex
import sys

translate = Yandex

class PYTRANSLATOR:
  def __init__(self, language):
    self.language=language
    self.yandex = Yandex

  def translate(self, text):
    result = self.yandex.translate(self.yandex, lang=self.language, text=text)
    return result[0]