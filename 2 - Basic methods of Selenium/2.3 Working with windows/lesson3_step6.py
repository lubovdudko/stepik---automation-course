#Задание: переход на новую вкладку

from selenium import webdriver
import math
import time
browser = webdriver.Chrome()


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    # находим кнопку и нажимаем
    submit = browser.find_element_by_xpath("//button[@class='trollface btn btn-primary']")
    submit.click()

    # переключаемся в новую вкладку браузера
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    # получаем значение x 
    x = browser.find_element_by_id("input_value").text
    y = calc(x)


    # находим поле и вводим значение 
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    # отправляем ответ
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    submit.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()