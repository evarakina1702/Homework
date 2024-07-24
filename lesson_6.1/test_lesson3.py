import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# def test_form_shopping():
driver.get("https://www.saucedemo.com/")
driver.implicitly_wait(10)
driver.maximize_window()
  
# Авторизоваться как пользователь "standard_user" и ввести пароль "secret_sauce"
driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
driver.find_element(By.CSS_SELECTOR, "#login-button").click()
sleep(2)

# Добавить в корзину 3 товара
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
sleep(2)

# Перейти в корзину
driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()
sleep(2)

# Нажать Checkout
driver.find_element(By.CSS_SELECTOR, "#checkout").click()
sleep(1)

# Заполнить форму своими данными
driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys("Елена")
driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys("Трегубова")
driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys("123456")
sleep(2)

# Нажать на кнопку "Continue"
driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()
sleep(1)

# Прочитать со страницы итоговую стоимость
txt = WebDriverWait(driver, "10").until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text

driver.find_element(By.CSS_SELECTOR, "#finish").click()

driver.quit()

assert txt == "Total: $58.29"

# Чтобы зыпустить "Pytest" , нужно в терминале ввести команду pytest и  нажать Enter
