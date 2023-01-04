from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
from selenium.webdriver.support.ui import Select
import math

link = "http://suninjuly.github.io/selects1.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")
    
    x_element = browser.find_element(By.ID, "num1")
    
    y_element = browser.find_element(By.ID, "num2")
    Sum = (int(x_element.text)+int(y_element.text))
    print(Sum)
    select = Select(browser.find_element(By.TAG_NAME,"select"))
    select.select_by_value(str(Sum)) # ищем элемент с текстом "Python"



    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла