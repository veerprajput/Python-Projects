from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = 'C:\Development\chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('https://en.wikipedia.org/wiki/Main_Page/')

# try:
#     anchors = driver.find_element_by_css_selector('#mp-welcomecount #articlecount a')
# except:
#     pass

# print(anchors.text)

# all_portals = driver.find_element_by_link_text('Content portals')
# # all_portals.click()

# search = driver.find_element_by_name('search')
# search.send_keys('Python')
# search.send_keys(Keys.ENTER)


# driver.quit()