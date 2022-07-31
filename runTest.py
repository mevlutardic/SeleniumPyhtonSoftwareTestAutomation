
import argparse
import random
parser = argparse.ArgumentParser()
parser.add_argument("Browser")
value = parser.parse_args()

from choseBrowser import ChoseBrowser # browser selector
from category import Category
from productPage import ProductPage
from productSelection import ProductSelection


class RunTest():

    def __init__(self,value):
        self.value=str(value)
        
    def main(self):
        url="https://www.lcwaikiki.com/tr-TR/TR"
        chose=ChoseBrowser()
        chose.setWebSite(url)
        chose.openBrowser(self.value)
        categoryUl='//*[@id="header__container"]/header/div[3]/nav/ul'
        cat=Category(categoryUl,chose.getDriver())
        cat.clickID(1)


        womenProductPageList=[
            '//*[@id="landingPageContainer"]/div/div[1]/div[1]/a[1]/img',
            '//*[@id="landingPageContainer"]/div/div[2]/div[3]/a/img',
            '//*[@id="landingPageContainer"]/div/div[2]/div[5]/a[1]/img',
            ]

        pr=ProductPage(womenProductPageList, chose.getDriver())
        pr.addProductPegeList('//*[@id="landingPageContainer"]/div/div[2]/div[5]/a[1]/img')

        pr.productClick(2)

        womenProductList=[
             '//*[@id="root"]/div/div[2]/div[2]/div[5]/div/div[2]/div[1]/a/div[1]/div[2]'

        ]
        prl=ProductSelection(womenProductList, chose.getDriver())

        pr.productPageClick(0)

        
        
        



if __name__ == '__main__':
    
    run=RunTest(value.Browser)
    run.main()