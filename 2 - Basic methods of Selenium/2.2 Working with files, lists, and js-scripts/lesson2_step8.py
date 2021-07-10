#Задание: загрузка файла

from selenium import webdriver
import os
import time
browser = webdriver.Chrome()

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    # находим поля и вводим значения 
    firstname = browser.find_element_by_name("firstname")
    firstname.send_keys("Fakename")
    lastname = browser.find_element_by_name("lastname")
    lastname.send_keys("Fakelastname")
    email = browser.find_element_by_name("email")
    email.send_keys("fakeemail@gmail.com")

    # находим путь к текущей директории и к файлу
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path=os.path.join(current_dir, 'file.txt')
    
    # находим поле добавление файла и выбираем файл
    file = browser.find_element_by_id("file")
    file.send_keys(file_path)

    # отправляем форму
    submit = browser.find_element_by_xpath("//button[@class='btn btn-primary']")
    submit.click()
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()