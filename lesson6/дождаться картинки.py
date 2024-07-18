from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Перейти на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождаться появления всех четырех картинок
element = WebDriverWait(driver, 12).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "#landscape"))
)

# Получить значение атрибута src у третьей картинки.
src = driver.find_element(By.CSS_SELECTOR, "#award").get_attribute("src")

# Вывести значение в консоль
print(src)

# Закрыть браузер
driver.quit()