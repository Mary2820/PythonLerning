import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service


@pytest.mark.run(order=2)
def test_metod_1():
    print('Метод 1')

    options = Options()
    driver = webdriver.Firefox(service=Service(), options=options)

    driver.get("https://www.instagram.com/")
    driver.implicitly_wait(3)
    button = driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[1]")
    button.click()