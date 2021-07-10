#Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Считаем значение переменной x
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)

    # Находим поле для ввода ответа и вводим его
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # Нажимаем чекбокс I'm the robot

    robot_checkbox = browser.find_element_by_css_selector("[for='robotCheckbox']")
    robot_checkbox.click()

    # Выбираем радиобаттон Robots rule

    robot_radio = browser.find_element_by_css_selector("[id='robotsRule']")
    robot_radio.click()
 
    # Отправляем форму

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()