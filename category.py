
from libraries import *

class Category():
    
    def __init__(self,categoryUl,driver):
        
        self.categoryUl=categoryUl
        self.driver=driver
         
        text_contents = [el.text for el in self.driver.find_elements_by_xpath(self.categoryUl)]
        self.categories=(str(text_contents[0]).split("\n"))

    def clickRandom(self):
        sleep(5)
        ID=random.randint(1, len(self.categories))
        li="//*[@id='header__container']/header/div[3]/nav/ul/li[{}]/a".format(ID)
        print(li)
        self.driver.find_element(By.XPATH,li).click()
        sleep(10)

    def clickID(self,ID):
        sleep(5)
        li="//*[@id='header__container']/header/div[3]/nav/ul/li[{}]/a".format(ID)
        self.driver.find_element(By.XPATH,li).click()
        sleep(10)

    def getCategoryUl(self):
        return self.categoryUl

    def setCategoryUl(self,categoryUl):
        self.categoryUl=categoryUl
        
    def getDriver(self):
        return self.driver

    def setDriver(self,driver):
        self.driver=driver

if __name__ == '__main__':
    pass