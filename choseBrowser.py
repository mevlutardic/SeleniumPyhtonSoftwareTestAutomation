from libraries import *

class ChoseBrowser():

    def __init__(self):

       
        # self.list_browser={
        #     "Chrome":webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
        #     "Edge":webdriver.Edge(EdgeChromiumDriverManager().install()),
        #     "Brave":Chrome(ChromeDriverManager(chrome_type=ChromeType.BRAVE).install()),
        #     "Firefox":webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()),
        #     "Chromium":webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
        # }

        self.list_browser = {
           
            "Chrome": webdriver.Chrome(service=ChromeService(ChromeDriverManager().install())),
            
        }
        self.browser=None
        self.driver=None    
        self.url=None


    def openBrowser(self,browser):
        self.driver=self.list_browser.get(browser)
        self.driver.get(self.url)
        self.driver.minimize_window()
        sleep(10)




    def setWebSite(self,url):
        self.url=url
        
    # You can add new browser with setNewBrowser methot.
    def setNewBrowser(self,Browser,BrowserServices):
        self.list_browser.update({str(Browser): BrowserServices})

    def get(self):
        return (self.browser)

    def getBrowserList(self):
        return self.list_browser

    def getDriver(self):
        return self.driver


if __name__ == '__main__':
    # url="https://www.lcwaikiki.com/tr-TR/TR"
    # a= ChoseBrowser("Chrome")
    # a.setWebSite(url)
    # a.openBrowser()
    pass
