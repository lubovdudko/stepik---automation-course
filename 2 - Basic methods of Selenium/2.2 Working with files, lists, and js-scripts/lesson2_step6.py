#Задание на execute_script

from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # получаем значение x 
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    # находим поле и вводим значение 
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # нажимаем чекбокс I'm the robot
    robot_checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    robot_checkbox.click()

 
    #скроллим до кнопки вниз
    button = browser.find_element_by_class_name("btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    # выбираем радиобаттон Robots rule

    robot_radio = browser.find_element_by_css_selector("[id='robotsRule']")
    robot_radio.click()

    # отправляем форму
    button.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()