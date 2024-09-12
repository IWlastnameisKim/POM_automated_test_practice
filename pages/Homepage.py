from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver        
        self.mainpageURL = 'https://fastcampus.co.kr/'
        self.username_login = (By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a')
        self.username_login_username = (By.XPATH, '/html/body/div[1]/header/div/div[2]/div/div[1]/em')
        self.searchbar_locator = (By.XPATH, '//*[@id="search-input"]')

    def try_login_btn(self) :
        self.driver.find_element(*self.username_login).click()


    