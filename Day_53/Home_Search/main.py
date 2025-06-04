from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth
import json

#First run this command in command prompt
#Also delete contents from chrome_profiles directory
#cd C:\Program Files\Google\Chrome\Application
#Then run this command chrome.exe --remote-debugging-port=4444 --user-data-dir="C:\Users\veerp\Documents\Veer_Learning\Python\Angela_Python_Course\python_codes\Projects\Home Search\chrome_profiles"

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_experimental_option('detach', True)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')

chrome_driver_path = 'C:\Development\chromedriver.exe'

FORM_LINK = 'https://docs.google.com/forms/d/e/1FAIpQLSfiSe57Ufhh0-d9rntRkxFkjrMCD61hoBCDXBsMbzb3RuwhWA/viewform?usp=sf_link'
#ZILLOW_LINK = 'https://www.zillow.com/folsom-ca/?searchQueryState=%7B%22usersSearchTerm%22%3A%22Folsom%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-121.39953019238281%2C%22east%22%3A-120.89278580761719%2C%22south%22%3A38.51050473309862%2C%22north%22%3A38.82092651392757%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11462%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A800000%2C%22max%22%3A1000000%7D%2C%22mp%22%3A%7B%22min%22%3A3663%2C%22max%22%3A4579%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D'
ZILLOW_LINK = 'https://www.zillow.com/folsom-ca/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Folsom%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-121.30542163063045%2C%22east%22%3A-120.97686175514217%2C%22south%22%3A38.56273127741911%2C%22north%22%3A38.739156190046934%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A11462%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A700000%2C%22max%22%3A1500000%7D%2C%22mp%22%3A%7B%22min%22%3A3056%2C%22max%22%3A6548%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%7D%2C%22isListVisible%22%3Atrue%7D'
# driver.get(ZILLOW_LINK)
req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'zgsession=1|999c402f-b553-4d4f-8f10-ed9456c113d4; _ga=GA1.2.871617979.1655828693; zg_anonymous_id=%22cceca175-ce7a-466b-9ec9-28740c1a5fa6%22; _pxvid=adea168c-f17e-11ec-b4fa-576d4c565362; pxcts=adea1e6f-f17e-11ec-b4fa-576d4c565362; _gcl_au=1.1.2009704425.1655828694; DoubleClickSession=true; __pdst=5f29280eaccf4ca695bf9211b87a7894; _cs_c=0; _pin_unauth=dWlkPU5ERTROalUxWldVdE16Y3daUzAwTTJWbUxUZzFZekV0TmpZd05qSTJZVGxrTVdObQ; G_ENABLED_IDPS=google; G_AUTHUSER_H=1; zjs_user_id=%22X1-ZU15zgu0hz7v37t_91vx9%22; zguid=24|%24bc60f57d-e5f4-479e-b0c5-ec2801f6296b; zjs_anonymous_id=%22bc60f57d-e5f4-479e-b0c5-ec2801f6296b%22; userid=X|3|11a71977991f35e5%7C3%7CyqIA-W3a4Va74o71gnAflJoiFtCY3RuI-A4_VIE9JIQ%3D; loginmemento=1|b9c820813fc859616fbb92364ee906f767d430ab9b5a2b665424c73ead175bf1; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEqzif%2F0stASnEoQMnBm3BmwQiLbjMns7kcoO73dsywOy8HuJ%2FLySOafELYrgJ4pPKPxRL55aD2pI; _gid=GA1.2.738295038.1657069826; KruxPixel=true; JSESSIONID=5E8A3F8CAA47F5CB2D3D0F68D4FEF50E; _hp2_ses_props.1215457233=%7B%22r%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22ts%22%3A1657069829080%2C%22d%22%3A%22www.zillow.com%22%2C%22h%22%3A%22%2F%22%7D; utag_main=v_id:01818714c64b000dcfe569cadbba0506f001706700d84$_sn:4$_se:1$_ss:1$_st:1657071628913$dc_visit:4$ses_id:1657069828913%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:us-west-2%3Bexp-session; _clck=1wss2sg|1|f2x|0; KruxAddition=true; _hp2_id.1215457233=%7B%22userId%22%3A%226850169963968916%22%2C%22pageviewId%22%3A%223535464406725098%22%2C%22sessionId%22%3A%226512224553807545%22%2C%22identity%22%3A%22X1-ZU15zgu0hz7v37t_91vx9%22%2C%22trackerVersion%22%3A%224.0%22%2C%22identityField%22%3Anull%2C%22isIdentified%22%3A1%7D; _cs_id=5936fd07-3b81-a809-81be-8e92c6dcfce2.1655828695.6.1657070347.1657069830.1.1689992695202; _cs_s=2.5.0.1657072147526; _px3=96ff6f1f3861559de5289dac1185beeeece4166aead9d561eff64ed47395e57a:izsmep4cnzqVz30i7iKXjsb6VFTtgKzHKeHuYiYUR6MQ2Ub07q0SWf8/775twAzUbjNmphVqAeA4uPxe+GuR5A==:1000:iVzMHGmXiDrcEtohOMrQIMIjzrs4ejfCDMCK4Yy3LDM0E1o1Wn/dPwIwJZJvDjIkVY0YVN7izosLlhQWMbsdkEr/rPxO8jVedRzdzIEgSSBQcWBCqC9NNDgwRoPFq3k+UcPUARVImGUeYkbgy/5NLndbTWC5pzeunXCou6hay9ra//hzbRMNYZtIePl0KZW+yBafPdVXfYk2Srvxkrmlcg==; _uetsid=6cca5f40fcc811eca27defc7139f963f; _uetvid=af16ebe0f17e11ec86f165ed7c2ef5b5; _clsk=174mw4n|1657070401266|13|0|j.clarity.ms/collect; AWSALB=VFiDIjruS2WXzg929YhxlQ3B/lMEOXfoxQUy/sRez4ZpzsHfKyPJzSZmw2PeXt7pkXjzedvLnuvOjkgyuKhBTE9KWcboYTELBNgUEZUmAlrO1VFdaYTrVmqPDnEV; AWSALBCORS=VFiDIjruS2WXzg929YhxlQ3B/lMEOXfoxQUy/sRez4ZpzsHfKyPJzSZmw2PeXt7pkXjzedvLnuvOjkgyuKhBTE9KWcboYTELBNgUEZUmAlrO1VFdaYTrVmqPDnEV; search=6|1659662415082%7Crect%3D38.70139394774237%252C-120.89810731030273%252C38.63035611853978%252C-121.39420868969727%26rid%3D11462%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26price%3D700000-1000000%26mp%3D3061-4583%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0911462%09%09%09%09%09%09',
    "referer": "https://www.zillow.com/",
    'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    "ser-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',",
    'accept-encoding': 'gzip, deflate, br',
    'upgrade-insecure-requests': '1',
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36",
}

params = {'searchQueryState': {"pagination":{},"usersSearchTerm":"Folsom, CA","mapBounds":{"west":-124.518960734375,"east":-117.773355265625,"south":34.48131000353457,"north":42.61950367425679},"mapZoom":12,"regionSelection":[{"regionId":11462,"regionType":6}],"isMapVisible":True,"filterState":{"price":{"min":700000,"max":1000000},"mp":{"min":3061,"max":4583},"ah":{"value": True},"sort":{"value":"globalrelevanceex"}, "isAllHomes": {'value': True}},"isListVisible": True}}

response = requests.get(url=ZILLOW_LINK, headers=req_headers, params=params)

zillow = response.text
# print(zillow)

soup = BeautifulSoup(zillow, 'html.parser')

data = json.loads(
    soup.select_one("script[data-zrr-shared-data-key]")
    .contents[0]
    .strip("!<>-")
)

# print(json.dumps(data, indent=4))


# for result in data["cat1"]["searchResults"]["listResults"]:
#     home_links = "{:<15} {:<50} {:<15}".format(result["detailUrl"])
#     addresses = "{:<15} {:<50} {:<15}".format(result["address"])
#     prices = "{:<15} {:<50} {:<15}".format(result["price"])

home_links = []
addresses = []
prices = []

for result in data["cat1"]["searchResults"]["listResults"]:
        home_links.append(str("{:<15}".format(result["detailUrl"])).strip())
        addresses.append(str("{:<50}".format(result["address"])).strip())
        prices.append(str("{:<15}".format(result["price"])).strip())

print(home_links)
print(addresses)
print(prices)

# deck = soup.find(name='ul', class_='List-c11n-8-69-1__sc-1smrmqp-0')
# print(len(deck))
# for card in deck.contents:
#     print(card)
#     script = card.find('script', {'type':'application/ld+json'})
#     if script:
#         script_json = json.loads(script.contents[0])
#         # print(script_json)
#         addresses = script_json['name']
#         print(addresses)

# prices1 = soup.find_all(name='div', class_='list-card-price')

# prices = [price.getText() for price in prices1][::-1]
# print(prices)

# addresses1 = soup.find_all(name='address', class_='list-card-addr')

# addresses = [price.getText() for price in addresses1][::-1]
# print(addresses)

# links1 = soup.find_all(name='a', class_='list-card-link')

# home_links = [str(link).split('href="')[1].split('" tabindex')[0] for link in links1][1::2][::-1]
# # print(links2)

# print(home_links)

opt = Options()
opt.add_experimental_option('debuggerAddress', 'localhost:4444')

driver = webdriver.Chrome(executable_path=chrome_driver_path, options=options, chrome_options=opt)
# stealth(driver,
#         languages=["en-US", "en"],
#         vendor="Google Inc.",
#         platform="Win32",
#         webgl_vendor="Intel Inc.",
#         renderer="Intel Iris OpenGL Engine",
#         fix_hairline=True,
#         )
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# executor_url = driver.command_executor._url
# session_id = driver.session_id

# print(session_id)
# print(executor_url)
# driver.maximize_window()
# driver.implicitly_wait(4)
# # driver.find_element(by=By.CLASS_NAME, value='action-link').click()
# # sign_in_button = driver.find_element(by=By.XPATH, value='//*[@id="text"]/button')
# driver.find_element(by=By.NAME, value='identifier').send_keys('veerprajput@gmail.com')
driver.get(FORM_LINK)
# driver.implicitly_wait(10)
# driver.find_element(by=By.XPATH, value='//*[@id="identifierNext"]/div/button/span').click()

for i in range(len(home_links)):
    address_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(addresses[i])
    price_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(prices[i])
    link_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(home_links[i])
    sumbit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    submit_another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()


driver.get('https://docs.google.com/forms/d/1ZFdB3fpdi42lUWkZvaThyWDhcWIP5N8iB0mEhmu91Ys/edit#responses')
sheet_icon = driver.find_element(By.XPATH, '//*[@id="ResponsesView"]/div/div[1]/div[1]/div[2]/div[1]/div/div/span').click()
click_create_button = driver.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[9]/div/div[2]/div[3]/div[2]/span/span').click()
