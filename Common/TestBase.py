import pytest

class TestBase: 
    @pytest.fixture(autouse=True)    
    def setup_base(self, test_setup) :    
        self.driver = test_setup["driver"]
        self.By = test_setup["By"]
        self.Keys = test_setup["Keys"]
        self.WebDriverWait = test_setup["WebDriverWait"]
        self.EC = test_setup["EC"]
        self.pd = test_setup["pd"]
        self.searchbar_locator = (self.By.XPATH,'//*[@id="search-input"]')
        self.AC = test_setup["AC"]
        self.time = test_setup["time"]
        
    def get_searchbar(self) :
        
        return self.driver.find_element(*self.searchbar_locator)
    
    def popup_close(self) : 
        try : 
            popup_close_locator = (self.By.XPATH, '/html/body/div[6]/div/div[2]/button[1]')
            self.driver.find_element(*popup_close_locator).click()
            
        except : pass
