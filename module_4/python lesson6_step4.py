from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by=By.CLASS_NAME, value='first')
    input1.send_keys("Saveliy")
    input2 = browser.find_element(by=By.CLASS_NAME, value='second')
    input2.send_keys("Medvedev")
    input3 = browser.find_element(by=By.CLASS_NAME, value='third')
    input3.send_keys("Irkutsk")
    button = browser.find_element(by=By.CSS_SELECTOR, value="button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element(by=By.TAG_NAME, value="h1")

    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()