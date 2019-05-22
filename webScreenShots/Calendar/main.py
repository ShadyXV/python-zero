from selenium import webdriver
import sys


DRIVER = '../chromedriver'
driver = webdriver.Chrome(DRIVER)

def screenShot(x) :
  baseurl = 'http://www.koshko.com/calendar/calendar' + str(x + 1) + '.shtml'
  driver.get(baseurl)
  return driver.save_screenshot('img/Calendar'+ str(x + 1)+ '.png');

try:
  for x in range(14):
    screen = screenShot(x)
  driver.quit()
except:
  print('error')