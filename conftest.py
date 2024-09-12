import pytest
import logging
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains as AC
import pandas as pd

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def driver() : 
    
    logger.info("Starting the setup fixture")

    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--incognito")

    
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    wait = WebDriverWait(driver, 10)        
    driver.get('https://fastcampus.co.kr/') # Replaced with actual url
    time.sleep(2)
    
    yield driver
@pytest.fixture(scope='session')
def test_setup(driver) : 
    return {
        "driver" : driver,
        "By" : By,
        "EC" : EC,
        "pd" : pd,
        "WebDriverWait" : WebDriverWait,
        "Keys" : Keys,
        "AC" : AC,
        "time" : time     
    }
    

    

