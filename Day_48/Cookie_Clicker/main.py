from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver_path = 'C:\Development\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver = webdriver.Chrome(ChromeDriverManager().install())

#edge_driver_path = "C:\Users\veerp\Downloads\edgedriver_win64\msedgedriver.exe"
#driver = webdriver.Edge(executable_path=edge_driver_path)



driver.get('http://orteil.dashnet.org/experiments/cookie/')
cookie = driver.find_element_by_id('cookie')

sec5 = time.time() + 10
sec300 = time.time() + 60*5


while True:
        cookie.click()
        cookies = str(driver.find_element_by_id('money').text)
        # print(type(cookies))
        if time.time() > sec5:
            divs = driver.find_elements_by_css_selector('#store b')
            # print(prices1)
            comma_prices = []
            for i in divs:
                comma_prices.append(i.text.split('-'))
            # print(prices)
    #     # letters = []
        
    #     driver.quit()
            prices = []
            for price in comma_prices:
                if ',' in price[-1]:
                    prices.append(price[-1].strip().replace(',', ''))
                else:
                    prices.append(price[-1])
            
            prices.pop(-1)
            
            # print(prices)
            for num in range(len(prices)):
                if ',' in cookies:
                    cookies = cookies.strip().replace(',', '')
                else:
                    pass
                if int(prices[num]) > int(cookies):
                    try:
                        divs[num - 1].click()
                    except:
                        pass
                    cookie.click()
                    cookie.click()
                    cookie.click()
                    cookie.click()
                    cookie.click()
            sec5 = time.time() + 5
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        cookie.click()
        if time.time() > sec300:
            print(driver.find_element_by_id('cps').text)
            driver.quit()
            break
                    
