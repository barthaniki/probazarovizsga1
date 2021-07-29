from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"
    driver.get(url)

    price = driver.find_element_by_id("price")
    tax = driver.find_element_by_id("tax")
    go_btn = driver.find_element_by_xpath('//button[@class="btn-go"]')

    # TC01 - correctness of the blank fill

    # test with blank fields
    assert price.get_attribute("value") == ""
    go_btn.click()
    assert tax.get_attribute("value") == ""
    alert_msg = driver.find_element_by_xpath('//*[@id="disclaimer"]/strong')
    assert alert_msg.text == "Enter the property value before clicking Go button."

    # TC02 - correct fill

    price.send_keys("3333")
    go_btn.click()

    # check data
    assert tax.get_attribute("value") == "16.665"

finally:
    driver.close()
    driver.quit()
