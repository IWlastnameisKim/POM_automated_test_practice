from selenium.webdriver.common.by import By
from pages.Homepage import HomePage


class LoginPage : 
    def __init__(self, driver):
        self.driver = driver        
        self.loginURL = 'https://fastcampus.co.kr/account/sign-in'
        self.ID_input = (By.ID, 'user-email')
        self.PW_input = (By.ID, 'user-password')
        self.loginbtn = (By.XPATH, '/html/body/div[1]/section/div/form/div[3]/button')

    def enter_ID(self, ID) : 
        self.driver.find_element(*self.ID_input).send_keys(ID)

    def enter_PW(self, PW) : 
        self.driver.find_element(*self.PW_input).send_keys(PW)

    def select_loginbtn(self) : 
        self.driver.find_element(*self.loginbtn).click()

    hompage = HomePage