from libraries import *

class ProductPage():

    def __init__(self,productPageList,driver):
        self.productList=productPageList
        self.driver=driver
   

    def productPageClick(self,item):
        
        path=self.productPageList[item]
        self.driver.find_element(By.XPATH,path).click()
        

    def addProductPegeList(self,item):
        self.productPageList.append(item)


    def getProductPageList(self):
        return self.productPageList