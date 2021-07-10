#Задание: поиск элемента по тексту в ссылке
from selenium import webdriver
import math
import time

link1 = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link1)
    link2 = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
    link2.click()
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Lubov")
    input2 = browser.find_element_by_name("last_name")
    input2.send_keys("Dudko")
    input3 = browser.find_element_by_class_name("city")
    input3.send_keys("Minsk")
    input4 = browser.find_element_by_id("country")
    input4.send_keys("Belarus")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(10)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
