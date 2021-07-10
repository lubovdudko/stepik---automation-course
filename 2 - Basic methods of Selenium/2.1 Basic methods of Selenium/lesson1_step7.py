#Задание: поиск сокровища с помощью get_attribute

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим картинку
    image = browser.find_element_by_id("treasure")

    # получаем значение x и высчитываем ответ
    x = image.get_attribute("valuex")
    y = calc(x)

    # находим поле для ввода ответа и вводим его
    input = browser.find_element_by_id("answer")
    input.send_keys(y)


    # нажимаем чекбокс I'm the robot
    robot_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    robot_checkbox.click()

    # выбираем радиобаттон Robots rule

    robot_radio = browser.find_element_by_css_selector("[id='robotsRule']")
    robot_radio.click()
 
    # отправляем форму

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
