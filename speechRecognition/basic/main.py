import speech_recognition as sr

test = sr.AudioFile('speech.wav')
r = sr.Recognizer()
with test as source:
  audio = r.record(source)
  res = r.recognize_google(audio)
  print(res)