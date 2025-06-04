# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# from webdriver_manager.chrome import ChromeDriverManager
# from PIL import Image
# import pyautogui

# options = webdriver.ChromeOptions()
# options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_experimental_option("detach", True)

# chrome_driver_path = 'C:\Development\chromedriver.exe'

# driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

# driver.get('chrome://dino')
# driver.find_element(by=By.XPATH, value='//*[@id="main-frame-error"]').send_keys(Keys.SPACE)

# while True:
#     pass

import pyautogui
import time
import keyboard

while 1:
    im = pyautogui.screenshot()
    screen = im.getpixel((71,217))
    x1 = im.getpixel((740, 326))
    x2 = im.getpixel((722, 326))
    x3 = im.getpixel((792, 326))
    x4 = im.getpixel((800, 326))
    y1 = im.getpixel((740, 273))
    y2 = im.getpixel((722, 273))
    y3 = im.getpixel((800, 273))
    y4 = im.getpixel((792, 273))
    
    if screen[0] == 255:
        if x1[0] != 255 or x2[0] != 255 or x3[0] != 255 or x4[0] != 255 or y1[0] != 255  or y2[0] != 255 or y3[0] != 255 or y4[0] != 255:
            pyautogui.press('space')
            time.sleep(0.01)
    
    
    if keyboard.is_pressed('esc')==True:
        break
    else:
        pass