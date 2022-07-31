from libraries import *

class ProductSelection():

    def __init__(self,productSelectionList,driver):
        self.productSelectionList=productSelectionList
        self.driver=driver
   

    def productSelectionClick(self,item):
        
        path=self.productSelectionList[item]
        self.driver.find_element(By.XPATH,path).click()
        

    def addProductSelectionList(self,item):
        self.productSelectionList.append(item)


    def getProductSelectionList(self):
        return self.productSelectionList