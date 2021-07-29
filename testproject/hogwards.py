from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"
    driver.get(url)

    # fill in input data fields
    passenger = driver.find_element_by_id("passenger")
    departure_date = driver.find_element_by_id("departure-date")
    departure_time = driver.find_element_by_id("departure-time")
    button = driver.find_element_by_id("issue-ticket")

    passenger.send_keys("KOVACS ETELKA")
    # departure = 2021.08.02. 10:32
    date_and_time = datetime(2021, 8, 2, 10, 32)
    departure_date.send_keys(date_and_time.strftime("%Y\t/%m/%d"))
    departure_time.send_keys(date_and_time.strftime("%I:%M"))
    button.click()

    # check ticket data
    passenger_name = driver.find_element_by_id("passenger-name")
    ticket_departure_date = driver.find_element_by_id("departure-date-text")
    ticket_departure_time = driver.find_element_by_id("departure-time-text")
    ticket_departure_date_side = driver.find_element_by_id("side-detparture-date")
    ticket_departure_time_side = driver.find_element_by_id("side-departure-time")

    assert passenger_name.text == "KOVACS ETELKA"
    assert ticket_departure_date.text == "2021-08-02"
    assert ticket_departure_time.text == "10:32AM"
    assert ticket_departure_date_side.text == "2021-08-02"
    assert ticket_departure_time_side.text == "10:32AM"

finally:
    driver.close()
    driver.quit()
