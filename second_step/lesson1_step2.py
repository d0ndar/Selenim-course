from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

    first1 = browser.find_element(By.ID, "num1")
    first = first1.text
    print(first)
    second1 = browser.find_element(By.ID, "num2")
    second = second1.text
    print(second)
    y = int(first) + int(second)
    
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(y)) # ищем элемент с текстом "Python"
    
    


    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()