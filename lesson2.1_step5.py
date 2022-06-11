from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    x_attribute = browser.find_element(By.CSS_SELECTOR, "#treasure").get_attribute("valuex")
    '''x_element = x_attribute.get_attribute("valuex")'''
    ''' x = x_element.text '''
    y = calc(x_attribute)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



finally:
    time.sleep(2)
    browser.close()
    browser.quit()
