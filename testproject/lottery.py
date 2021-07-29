import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

options = Options()

options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    url = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"
    driver.get(url)

    section = driver.find_element_by_id("container")
    generate_btn = driver.find_element_by_id("draw-number")
    reset_btn = driver.find_element_by_id("reset-numbers")

    # TC01 - the numbers are unknown

    assert section.is_displayed()
    # assert not driver.find_element_by_class_name("balls").is_displayed()
    time.sleep(2)

    # TC02 - lottery works

    for _ in range(6):
        generate_btn.click()

    balls = driver.find_elements_by_class_name("balls")

    list_nums = []
    for ball in balls:
        ball = ball.text
        list_nums.append(int(ball))

    print(list_nums)
    assert len(list_nums) == 6

    for nums in list_nums:
        assert 1 <= nums <= 59
    time.sleep(2)

    # TC03

    generate_btn.click()

    list_nums2 = []
    for ball in balls:
        ball = ball.text
        list_nums2.append(int(ball))

    print(list_nums2)
    assert len(list_nums2) == 6

    reset_btn.click()

    # assert not driver.find_element_by_class_name("balls").is_displayed()

# handle the element not existing
except NoSuchElementException:
    pass

finally:
    driver.close()
    driver.quit()
