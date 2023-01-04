from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)  
    
    wait = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),'$100'))
        

    button = browser.find_element(By.ID, "book" )
    button.click()

    x_element = browser.find_element(By.ID, "input_value")
    y = calc(x_element.text)
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)
    button = browser.find_element(By.CSS_SELECTOR, "button[id='solve']")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



