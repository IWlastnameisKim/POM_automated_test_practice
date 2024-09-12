import pytest
from Common.TestBase import TestBase
from pages.Homepage import HomePage
from pages.Loginpage import LoginPage
import pytest_dependency

@pytest.mark.usefixtures("test_setup")
class Test_Login_003(TestBase) :     
    @pytest.mark.dependency(depends=["test_login_001_valid"], scope = "session")    
    
    def test_login_003(self) : 
        home_page = HomePage(self.driver)
        
        for i in range(1,6) :  
            self.driver.find_element(*home_page.username_login_username).click()
            mypage_menu = f'/html/body/div[1]/header/div/div[2]/div/div[3]/div[{i}]'
            self.driver.find_element(self.By.XPATH, mypage_menu).click() 
            self.WebDriverWait(self.driver,10).until(self.EC.visibility_of_all_elements_located)    
            self.time.sleep(3)      
            if i == 1 :
                assert "me/course" in self.driver.current_url, "내 강의 보기 url 불일치"
            elif i == 2 : 
                assert "me/enrolled" in self.driver.current_url, "결제 대기 강의 url 불일치"                  
            elif  i == 3 : 
                assert "me/payment/paid" in self.driver.current_url, "거래내역 url 불일치"
            elif  i == 4 : pass
            elif  i == 5 : 
                try : 
                    self.popup_close
                    self.driver.find_element(home_page.username_login_username)
                    pytest.fail("로그아웃 실패")
                except : 
                    pass
                

