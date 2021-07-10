#Задание: работа с выпадающим списком

from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # получаем значение x и y и высчитываем ответ
    x = browser.find_element_by_id("num1").text
    y = browser.find_element_by_id("num2").text
    z=str(int(x)+int(y))

    # открываем дропдаун и выбираем из него значение z
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_value(z)
 
    # отправляем форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
