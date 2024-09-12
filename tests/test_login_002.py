import pytest
import pytest_dependency
from pages.Loginpage import LoginPage
from pages.Homepage import HomePage
from Common.TestBase import TestBase
import time

@pytest.mark.usefixtures("test_setup")



class TestLogin002(TestBase):
    @pytest.mark.dependency(depends=["test_login_001_valid"], scope="session")    
    def test_login_002(self):
        
        login_page = LoginPage(self.driver)
        home_page = HomePage(self.driver)

        try:
            # home_user_name_locator = '/html/body/div[1]/header/div/div[2]/div/div[1]/em'            
            self.driver.find_element(*home_page.username_login_username).click()
            #self.WebDriverWait(self.driver, 10).unitl(self.EC.element_to_be_clickable((self.By.XPATH, '/html/body/div[2]/header/div/div[2]/div/div[3]')))
            time.sleep(2)
         
            user_menu_elements = self.driver.find_elements(self.By.CSS_SELECTOR, 'div.user-menu__menu-item')
            temp = len(user_menu_elements)
            assert len(user_menu_elements) >= 4, temp

        except Exception as mypage_error:            
            pytest.fail(f"Error in user menu verification: {mypage_error}")

