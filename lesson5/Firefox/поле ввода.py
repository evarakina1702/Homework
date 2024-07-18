from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/inputs")

# Ввести в поле текст 1000
search_field = "input[type='number']"
search_input = driver.find_element(By.CSS_SELECTOR, search_field)
sleep(2)
search_input.send_keys("1000")
sleep(2)

# Очистить это поле методом clear
search_input.clear()
sleep(2)

# Ввести в это же поле текст 999
search_input.send_keys("999")

sleep(5)