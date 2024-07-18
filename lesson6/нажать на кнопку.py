from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Перейти на страницу 
driver.implicitly_wait(25)

driver.get("http://www.uitestingplayground.com/ajax")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получить текст из зеленой плашки
content = driver.find_element(By.CSS_SELECTOR, "#content")
txt = content.find_element(By.CSS_SELECTOR, "p.bg-success").text

# Вывести его в консоль
print(txt) 

# Закрыть браузер
driver.quit()