from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, math
from selenium import webdriver

from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait2.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
    button.click()

    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(2)
    browser.close()
    browser.quit()
