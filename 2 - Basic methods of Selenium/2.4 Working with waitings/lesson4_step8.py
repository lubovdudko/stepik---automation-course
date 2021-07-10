#Задание: ждем нужный текст на странице

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time
browser = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    # находим кнопку Book
    button = browser.find_element_by_id("book")

    # говорим Selenium проверять в течение 12 секунд, пока не будет нужной цены
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))
    button.click()

    # получаем значение x 
    x = browser.find_element_by_id("input_value").text
    y = calc(x)

    # находим поле и вводим значение 
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # отправляем ответ
    submit = browser.find_element_by_id("solve")
    submit.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()