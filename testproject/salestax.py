from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"
    driver.get(url)

    subtotal_btn = driver.find_element_by_id("subtotalBtn")
    gtotal_btn = driver.find_element_by_id("gtotalBtn")
    salestax = driver.find_element_by_id("salestax")
    subtotal = driver.find_element_by_id("subtotal")
    gtotal = driver.find_element_by_id("gtotal")
    quantity = driver.find_element_by_id("quantity")

    # TC01 - correctness of the blank fill

    # no blank fields check, just click on buttons
    subtotal_btn.click()
    gtotal_btn.click()

    # check data
    assert salestax.get_attribute("value") == "0.00"
    assert gtotal.get_attribute("value") == "4.95"

    # TC02 - test with "6" x 6" Volkanik Ice" data

    driver.find_element_by_xpath('//*[@id="Proditem"]/option[2]').click()
    quantity.send_keys("1")
    subtotal_btn.click()
    gtotal_btn.click()

    # check data
    assert subtotal.get_attribute("value") == "4.95"
    assert gtotal.get_attribute("value") == "9.90"

finally:
    driver.close()
    driver.quit()
