# from selenium import webdriver

# chrome_driver_path = 'C:\Development\chromedriver.exe'
# driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get('https://www.python.org/')

# try:
#     event_times = driver.find_elements_by_css_selector('.event-widget time')
#     names = driver.find_elements_by_css_selector('.event-widget li a')
#     events = {}
# except:
#     pass
# for num in range(len(event_times)):
#     events[num] = {
#         'time': event_times[num].text,
#         'name': names[num].text
#     }

# print(events)
# driver.quit()