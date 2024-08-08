from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class StorePage:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get("https://www.saucedemo.com/")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

   # Авторизоваться как пользователь "standard_user" и ввести пароль "secret_sauce"
    def autorization(self, name = "standard_user", password = "secret_sauce"):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    # Добавить в корзину 3 товара
    def add_products(self):
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        counter = 'Total: $58.29'
        return counter

    # Перейти в корзину
    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, 'a[data-test="shopping-cart-link"]').click()

    # Нажать Checkout 
        self.driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    # Заполнить форму своими данными
    def personal_information(self, name: str, last_name: str, index: int):
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="firstName"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="lastName"]').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="postalCode"]').send_keys(index)
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="continue"]').click()

    # Вызов метода для ожидания элемента в течение 10 секунд
    def waiting_total_cost(self):
        txt = WebDriverWait(self.driver, "10").until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))).text
        return txt


    def close(self):
        self.driver.find_element(By.CSS_SELECTOR, "#finish").click()
        self.driver.quit()
