from selenium import webdriver
from selenium.webdriver.common.by import By
import time



try: 
    link = "http://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    browser.implicitly_wait(5) #there is waiting 

    button = browser.find_element(By.ID, "button")
    button.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()



