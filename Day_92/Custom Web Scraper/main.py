from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

chrome_driver_path = 'C:\Development\chromedriver.exe'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get('https://stats.espncricinfo.com/ci/content/records/83548.html')

names_selenium_elements = driver.find_elements(by=By.CLASS_NAME, value='data-link')
names = {
        'Player Name': [],
        'Playing Span': [],
        'Matches Played': [],
        'Innings Batted': [],
        'Not Outs': [],
        'Runs': [],
        'Highest Inning Score': [],
        'Batting Average': [],
        'Balls Faced': [],
        'Batting Strike Rate': [],
        'Hundreds Scored': [],
        'Fifties Scored': [],
        'Ducks Scored': [],
        'Boundries 4s': [],
        'Boundries 6s': []
    }
for i in range(len(names_selenium_elements)):
    names['Player Name'].append(names_selenium_elements[i].text)
    names['Playing Span'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[2]').text)
    names['Matches Played'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[3]').text)
    names['Innings Batted'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[4]').text)
    names['Not Outs'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[5]').text)
    names['Runs'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[6]/b').text)
    names['Highest Inning Score'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[7]').text)
    names['Batting Average'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[8]').text)
    names['Balls Faced'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[9]').text)
    names['Batting Strike Rate'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[10]').text)
    names['Hundreds Scored'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[11]').text)
    names['Fifties Scored'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[12]').text)
    names['Ducks Scored'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[13]').text)
    names['Boundries 4s'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[14]').text)
    names['Boundries 6s'].append(driver.find_element(by=By.XPATH, value=f'//*[@id="ciHomeContentlhs"]/div[3]/div/table[1]/tbody/tr[{i + 1}]/td[15]').text)
print(names)

pd.DataFrame(names).to_csv('Most_Total_Runs_ODI_Cricket.csv')