import pytest
import time
from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
from Common.TestBase import TestBase

@pytest.mark.usefixtures("test_setup")

class TestHomepage(TestBase) : 
    def test_homepage_valid(self) : 
        hompage = HomePage(self.driver)
        self.driver.get('https://fastcampus.co.kr')
        self.driver.implicitly_wait(5)
        try :
            hompage.popup_close()
        except Exception as e :
            print(e)
