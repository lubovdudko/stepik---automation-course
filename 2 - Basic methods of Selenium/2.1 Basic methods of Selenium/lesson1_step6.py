#Метод get_attribute

from selenium import webdriver
import time


try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)


    # Находим радиобаттон People rule и проверяем его состояние по дефолту
    people_radio = browser.find_element_by_id("peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # Находим радиобаттон Robot rule и проверяем его состояние по дефолту
    robot_radio = browser.find_element_by_id("robotsRule")
    robot_checked = robot_radio.get_attribute("checked")
    print("value of robot radio: ", robot_checked)
    assert robot_checked is None

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()