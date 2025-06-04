from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# chrome_driver_path = 'C:\Development\chromedriver.exe'
SIMILAR_ACCOUNT = 'rajputketa'

class InstaFollower():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.instagram.com')
        # self.driver.get('https://www.google.com')
    # def sign_in(self):
    #     time.sleep(2)
    #     sign_in_button = self.driver.find_element(by=By.XPATH, value='//*[@id="gb"]/div/div[2]/a')
    #     sign_in_button.click()
    #     time.sleep(2)
    #     email = self.driver.find_element(by=By.XPATH, value='//*[@id="identifierId"]')
    #     email.send_keys('wishtoinvest@gmail.com')
    #     nextb = self.driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span')
    #     nextb.click()
    #     time.sleep(50)
    def login(self):
        time.sleep(2)
        username = self.driver.find_element(by=By.NAME, value='username')
        username.send_keys('wishtoinvest@gmail.com')
        time.sleep(2)
        password = self.driver.find_element(by=By.NAME, value='password')
        password.send_keys('wishtolearn')
        time.sleep(2)
        login = self.driver.find_element(by=By.XPATH, value='//*[@id="loginForm"]/div/div[3]')
        login.click()
        time.sleep(2)
        notnow = self.driver.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[1]')
        notnow.click()
        time.sleep(5)
        # time.sleep(20)
        # othernotnow = self.driver.find_element(by=By.CLASS_NAME, value='_a9--')
        # othernotnow.click()
    
    def find_followers(self):
        time.sleep(2)
        # search_click = self.driver.find_element(by=By.XPATH, value='//*[@id="mount_0_0_hm"]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]')
        # search_click.click()
        search_button = self.driver.find_element(by=By.CLASS_NAME, value='xjbqb8w')
        search_button.click()
        time.sleep(2)
        search = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/input')
        search.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        account = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a')
        account.click()
        time.sleep(50)
        
        # time.sleep(0.8)
        # followers = self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[1]/div/div/div[1]/div[1]/section/main/div/header/section/ul/li[2]/a')
        # followers.click()
        
        # time.sleep(3)
        # popup = self.driver.find_elements(by=By.XPATH, value='/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[2]/ul/div/li[2]/div/div[3]/button')
        # buttons = self.driver.find_element(by=By.XPATH, value='//div[@class="_aaes"]//*//*')
        # names = self.driver.find_elements(by=By.CLASS_NAME, value='_aade')[18:]
        # # scroller = self.driver.find_element(by=By.CLASS_NAME, value='_anno')
        
        # iterations = 0
        
        # for d in names:
        #     if d.text != 'Follow':
        #         print(len(buttons))
        #         if d.text == 'shreeda07':
        #             buttons.click()
        #     iterations += 1
        #     if iterations % 10 == 0:
        #         time.sleep(0.8)
                
            
        # for person in popup:
        #     if person.text == 'Follow':
        #         print(person.text)
        #         print(len(popup))
                # person.send_keys(Keys.END)
        # self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", popup)


instagram = InstaFollower()
# instagram.sign_in()
instagram.login()
instagram.find_followers()
