import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from DataPage import DataPage


def test_form_elements():
  
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    
        data_page = DataPage(driver)

        data_page.data_types("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", "Москва", "Россия", "QA", "SkyPro")
        data_page.zip_code_red()
        data_page.other_fields_green()
        data_page.close_driver()