from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    num1 = browser.find_element(By.CSS_SELECTOR, "#num1").text
    num2 = browser.find_element(By.CSS_SELECTOR, "#num2").text
    summa = int(num1) + int(num2)
    time.sleep(1)

    Select(browser.find_element(By.TAG_NAME, "select")).select_by_value(str(summa))
    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(2)
    browser.quit()
