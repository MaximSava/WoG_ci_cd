import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# load .env variables
load_dotenv()

# Webdriver env
CHROME_WEBDRIVER_PATH = os.getenv('CHROME_WEBDRIVER_PATH')


def test_scores_service(app_url):
    # Configuration for driver
    print(app_url)
    chrome_options = webdriver.ChromeOptions()
    # webdriver remote docker-selenium from https://github.com/SeleniumHQ/docker-selenium
    chrome_driver = webdriver.Remote(command_executor='http://selenium-chrome:4444', options=chrome_options)
    # get site's score
    chrome_driver.get(app_url)
    score_xpath = "//*[@id=\"score\"]"
    score = WebDriverWait(chrome_driver, 10).until(
        ec.visibility_of_element_located((By.XPATH, score_xpath)))
    if score:
        score_value = int(chrome_driver.find_element(By.XPATH, score_xpath).text)
        if 1 <= score_value <= 1000:
            chrome_driver.close()
            chrome_driver.quit()
            return True
        else:
            chrome_driver.close()
            chrome_driver.quit()
            return False


def main_function():
    """
    main_function to call our tests function. The main function will return -1 as an OS exit
    code if the tests failed and 0 if they passed.
    """
    code = test_scores_service(' http://worldofgames:5000/')
    if code:
        print(0)
        return 0
    else:
        print(-1)
        os.system(exit())
        return -1


if __name__ == "__main__":
    main_function()
