from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"
    driver.get(url)

    email = driver.find_element_by_xpath('//input[@type="email"]')
    next_btn = driver.find_element_by_xpath('//input[@type="button"]')
    hours = driver.find_element_by_xpath('//input[@placeholder="hours"]')
    minutes = driver.find_element_by_xpath('//input[@placeholder="minutes"]')
    message = driver.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
    work_type = driver.find_element_by_xpath('//*[@id="dropDown"]/option')

    # TC01 - correctness of the blank fill

    # test with blank email field
    assert not next_btn.is_enabled()

    # test with bad format email address
    assert email.get_attribute("value") == ""
    email.send_keys("kissnoragmail.com")
    assert not next_btn.is_enabled()

    # TC02 - correct fill

    email.clear()
    email.send_keys("test@bela.hu")
    hours.send_keys(2)
    minutes.send_keys(0)
    message.send_keys("working hard")
    work_type.click()
    next_btn.click()

    # check correctness of time
    assert hours.get_attribute("value") == "2"
    assert minutes.get_attribute("value") == "0"

finally:
    driver.close()
    driver.quit()
