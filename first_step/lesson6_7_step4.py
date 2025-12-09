from selenium import webdriver
from selenium.webdriver.common.by import By
import time 



link = "http://suninjuly.github.io/find_xpath_form"

try:
    

    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Михаил")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Попов")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Новодвинск")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Россия")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
