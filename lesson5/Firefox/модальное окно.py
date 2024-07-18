from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.get("http://the-internet.herokuapp.com/entry_ad")
sleep(3)

#В модальном окне нажать на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

sleep(5)