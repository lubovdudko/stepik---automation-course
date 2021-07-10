#Пример задачи для execute_script

from selenium import webdriver
import time
browser = webdriver.Chrome()
try:
  link = "https://SunInJuly.github.io/execute_script.html"
  browser.get(link)
  button = browser.find_element_by_tag_name("button")
  browser.execute_script("return arguments[0].scrollIntoView(true);", button)
  time.sleep(5)
  button.click()
finally:
  browser.quit()