from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements_by_css_selector("[type=text")
    for element in elements:
        element.send_keys("Мой ответ")

    button = browser.find_element(by=By.CSS_SELECTOR, value='[type=submit]')
    button.click()

finally:
    time.sleep(30)
    browser.quit()

