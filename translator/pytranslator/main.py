from yandex import Yandex
import sys

translate = Yandex

def main():
  try :
    language = sys.argv[1]
    text = sys.argv[2]
    result = translate.translate(translate, lang=language, text=text)
    return result[0]
  except IndexError:
    print("Command : python main.py { language code } { text here }")

print(main())