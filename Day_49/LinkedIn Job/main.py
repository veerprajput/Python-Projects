from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
import time

options = webdriver.ChromeOptions()
# options.add_experimental_option()

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options)

driver.get('https://www.linkedin.com/jobs/search/?f_AL=true&f_E=3&geoId=102095887&keywords=python%20developer&location=California%2C%20United%20States')

time.sleep(1)

def login():
    global driver
    sign_in = driver.find_element_by_css_selector('.cta-modal__primary-btn')

    sign_in.click()

    email_input = driver.find_element_by_name('session_key')
    email_input.send_keys('veerprajput@gmail.com')
    password_input = driver.find_element_by_name('session_password')
    password_input.send_keys('Stem@11854')

    other_sign_in = driver.find_element_by_css_selector('div button')
    other_sign_in.click()

login()

time.sleep(1)






job_applications = driver.find_elements_by_css_selector('.job-card-container--clickable')

for application in job_applications:
        save_button = driver.find_element_by_css_selector('.jobs-save-button')
        save_button.click()
        time.sleep(3)
        try:
            application.click() 
        except:
            continue
        else:
        # a = ActionChains(driver).move_to_element(driver.find_element_by_css_selector(application)).perform()
        
        # easy_apply_button = driver.find_element_by_class_name('jobs-apply-button')
        # easy_apply_button.click()

        # try:
        #     phone_number = driver.find_element_by_id('#ember335')
        #     phone_number.send_keys('9213522234')
        #     print('Phone number')
        # except:
        #     next_button = driver.find_element_by_class_name('artdeco-button .artdeco-button--2 .artdeco-button--primary .ember-view')
        #     next_button.click()


            save_button = driver.find_element_by_css_selector('.jobs-save-button')
            save_button.click()
            # hide_button = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div[1]/div[1]/div[3]/div/button')
            # hide_button.click()

            # x_button = driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[1]/div/div/button')
            # x_button.click()
            print(application)
