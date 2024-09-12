import pytest
import time
from pages.Loginpage import LoginPage
from pages.Homepage import HomePage
from Common.TestBase import TestBase

@pytest.mark.usefixtures("test_setup")


class TestLogin_001(TestBase):
    @pytest.mark.dependency(name="test_login_001_valid", scope="session")
    def test_login_valid(self):
        login_page = LoginPage(self.driver)        
        self.driver.get('TestURL') # 테스트 URL 로 변경해주세요
        self.WebDriverWait(self.driver, 10).until(self.EC.visibility_of_all_elements_located)
        login_page.enter_ID(ID') # 테스트할 ID로 변경해주세요
        time.sleep(1)
        login_page.enter_PW('PW') # 테스트할 PW로 변경해주세요
        time.sleep(1)
        login_page.select_loginbtn()
        time.sleep(1)
        self.WebDriverWait(self.driver, 10).until(self.EC.visibility_of_any_elements_located)

    
    def test_LoginCHK(self):
        try : 
            # self.WebDriverWait(self.driver, 10).until(self.EC.visibility_of_elemnts_
            self.popup_close()
            self.WebDriverWait(self.driver, 10).until(self.EC.visibility_of_any_elements_located)
            time.sleep(1)
        except Exception as e :
            pass
        try:
            home_login_button = self.driver.find_elements(self.By.XPATH, '/html/body/div[2]/header/div/div[2]/div/a')
            assert len(home_login_button) == 0, "Login button is still visible"

            home_user_name_locator = '/html/body/div[1]/header/div/div[2]/div/div[1]/em'
            assert len(self.driver.find_elements(self.By.XPATH, home_user_name_locator)) > 0, "Username not visible"
        except Exception as e:
            with open('./loginfail.txt', 'w') as f:
                f.write(f"An error occurred: {e}")
            pytest.fail(f"An error occurred: {e}")
