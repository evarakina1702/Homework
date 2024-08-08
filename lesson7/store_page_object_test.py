from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Page.StorePage import StorePage

def test_form_online_store():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    online_store_page = StorePage(driver)
    online_store_page.authorization("standard_user", "secret_sauce")
    to_be = online_store_page.add_products()
    online_store_page.go_to_cart()
    online_store_page.personal_information("Елена", "Трегубова", "123456")
    as_is = online_store_page.total_cost()
    assert as_is == to_be
    online_store_page.close()
