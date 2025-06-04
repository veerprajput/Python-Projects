from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

##Extra: Can Delete Later
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options

import time

PROMISED_DOWN = 600
PROMISED_UP = 50
TWITTER_EMAIL = 'wishtoinvest@gmail.com'
TWITTER_PASSWORD = 'technocrat$4'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver_path = 'C:\Development\chromedriver.exe'

class InternetSpeedTwitterBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)
        self.driver.get('https://www.speedtest.net/')
        self.up = 374.89
        self.down = 11.66
    
    def get_internet_speed(self):
        go = self.driver.find_element_by_class_name('js-start-test')
        go.click()
        time.sleep(42)
        
        self.down = self.driver.find_element_by_class_name('download-speed').text
        self.up = self.driver.find_element_by_class_name('upload-speed').text
        
        print(f'{self.down}/{self.up}')
    
    def tweet_at_provider(self):
        self.driver.get('https://www.twitter.com')
        # time.sleep(3)
        # email_field = self.driver.find_element_by_class_name('r-1awozwy')
        # email_field.click()
        # enter_input = self.driver.find_element_by_class_name('r-30o5oe')
        # enter_input.send_keys(f'{TWITTER_EMAIL}')
        # next_button = self.driver.find_element_by_class_name('r-b88u0q')
        # next_button.click()
        time.sleep(3)
        try:
            sign_in = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div')
            sign_in.click()
            sign_in.click()
        except:
            time.sleep(3)
            email_field = self.driver.find_element_by_class_name('r-1awozwy')
            email_field.click()
            time.sleep(2)
            enter_input = self.driver.find_element_by_class_name('r-30o5oe')
            enter_input.send_keys(f'wishtoinvest')
            # time.sleep(2)
            next_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')
            print(next_button)
            next_button.click()
            time.sleep(4)
            password_input = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
            password_input.send_keys(f'technocrat$4')
            login_button = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div')
            login_button.click()
            
            time.sleep(5)
            # wait = WebDriverWait(self.driver, 10)
            # tweet_input = self.driver.find_element_by_xpath(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            # tweet_input = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
            # tweet_input = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
            # tweet_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')))
            # tweet_input = WebDriverWait(self.driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-1dbjc4n r-xoduu5 r-1sp51qo r-mk0yit r-13qz1uu']")))
            # tweet_input.click()
            
            # ActionChains(self.driver).move_to_element(tweet_input).click(tweet_input).send_keys(f'Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up').perform()
            # tweet = self.driver.find_element(by=By.XPATH, value='//*[@id="placeholder-bbfkt"]')
            # tweet.send_keys(f'Hey Internet Provider, why is my internet speed {self.down} down/{self.up} up when I pay for {PROMISED_DOWN} down/{PROMISED_UP} up')
            
            tweet_click = self.driver.find_element(by=By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]')
            tweet_click.click()
            tweet_compose = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div')
            tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
            tweet_compose.send_keys(tweet)
            time.sleep(3)

            tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]')
            tweet_button.click()
        print(f'But I pay for {PROMISED_DOWN}/{PROMISED_UP}')


o = InternetSpeedTwitterBot()
o.get_internet_speed()
o.tweet_at_provider()
