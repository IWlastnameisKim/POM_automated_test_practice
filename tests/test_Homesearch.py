import time
import pytest
import pandas as pd
from Common.TestBase import TestBase
from pages.Homepage import HomePage

@pytest.mark.usefixtures("test_setup")

class Test_HomeSearch(TestBase) : 
    def test_homesearch(self) :
        self.popup_close()     
        searchbar_locator = (self.By.XPATH, '//*[@id="search-input"]')  
        try :            
            self.driver.find_element(*searchbar_locator).click()
            self.driver.find_element(*searchbar_locator).send_keys("검색테스트1")
            time.sleep(1)
            self.driver.find_element(*searchbar_locator).send_keys(self.Keys.ENTER)
        except Exception as Error1 :
            pytest.fail(Error1)

        self.WebDriverWait(self.driver, 10).until(
            self.EC.visibility_of_element_located((self.By.XPATH, '//*[@id="main"]/div/section/div/p/span')))
        time.sleep(2)
        assert str("검색테스트1") in self.driver.find_element(self.By.XPATH, '//*[@id="main"]/div/section/div/p/span').text, "검색된 항목 없을 때 검색어 미노출"


        try :             
            self.driver.find_element(*searchbar_locator).click()
            time.sleep(1)
            self.driver.find_element(*searchbar_locator).clear()
            time.sleep(1)
            self.driver.find_element(*searchbar_locator).send_keys("파이썬")
            self.driver.find_element(*searchbar_locator).send_keys(self.Keys.ENTER)
            time.sleep(2)
        except Exception as e : 
            pytest.fail(f'검색어 입력 후 검색 동작 fail : ',e )


            self.driver.implicitly_wait(5)
            
        assert self.driver.find_elements(self.By.XPATH, '//*[@id="main"]/div/section/div/div[2]/div[1]/a[1]/img') , "강의 검색 실패"
        try :                  


            self.driver.find_element(*searchbar_locator).click()
            time.sleep(2)
            assert not self.driver.find_elements(self.By.CLASS_NAME, 'search-recent__list'), "검색 기록 미노출"
            
                
            assert self.driver.find_element(self.By.XPATH, '/html/body/div[1]/header/div/div[1]/div[1]/div/div[1]/ul/li/a').text == "파이썬", "검색 기록 FAIL"
                
        except Exception as Error3 :
            print(Error3)

        try :
            self.driver.find_element(self.By.CLASS_NAME, 'recommend-search__list')
            print("추천 검색어 노출 PASS")
        except : 
            pytest.fail(f"추천 검색어 미노출")

        

