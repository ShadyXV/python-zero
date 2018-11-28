from selenium import webdriver
import sys


try:
  DRIVER = '../chromedriver'
  driver = webdriver.Chrome(DRIVER)
  driver.get(sys.argv[1])
  screenshot = driver.save_screenshot('my_screenshot.png')
  driver.quit()
except:
  print('Command: python main.py <URL>')