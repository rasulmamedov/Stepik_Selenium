from selenium import webdriver
import time

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element(By.CSS_SELECTOR, ".form-control.first")
    input1.send_keys("Ivan")

    input2 = browser.find_element(By.CSS_SELECTOR, ".form-control.second")
    input2.send_keys("Petrov")

    input3 = browser.find_element(By.CSS_SELECTOR, ".form-control.third")
    input3.send_keys("Smolensk")

    custom_assert_input1 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']")
    ustom_assert_input2 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']")
    custom_assert_input3 = browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    time.sleep(2)
    button.click()
    time.sleep(2)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
