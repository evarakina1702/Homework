import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# def test_form_elements():
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.implicitly_wait(4)
driver.maximize_window()
    
driver.find_element(By.NAME, "first-name").send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "zip-code").send_keys("")
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("Qa")
driver.find_element(By.NAME, "company").send_keys("SkyPro")
sleep(3)

# Нажать на кнопку "Submit"
WebDriverWait(driver, 40, 0.1).until(EC.element_to_be_clickable((By.TAG_NAME, "button"))).click()
sleep(2)  

# Проверить, что поле zip-code подсвечено красным
zip_code_color = driver.find_element(By.CSS_SELECTOR, "#zip-code").value_of_css_property("background-color")
assert zip_code_color == 'rgba(248, 215, 218, 1)', "Zip code field is not highlighted as invalid"

# Проверить, что все остальные поля подсвечены зеленым
other_fields = ["#first-name", "#last-name", "#address", "#e-mail", "#phone", "#city", "#country", "#job-position", "#company"]
for field in other_fields:
    field_color = driver.find_element(By.CSS_SELECTOR, field).value_of_css_property("background-color")
    assert field_color == 'rgba(209, 231, 221, 1)', f"{field} is incorrectly marked as invalid"
    
driver.quit()

# Чтобы зыпустить "Pytest" , нужно в терминале ввести команду pytest и  нажать Enter
