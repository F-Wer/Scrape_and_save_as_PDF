import json
import time

from selenium import webdriver
with open("D:/aaaaa.txt") as file:
    count = sum(1 for _ in file)
file.close()
str_c = str(count)
i = 1
chrome_options = webdriver.ChromeOptions()
settings = {
       "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2
    }
prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(settings)}
chrome_options.add_experimental_option('prefs', prefs)
chrome_options.add_argument('--kiosk-printing')
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("-incongnito")
driver = webdriver.Chrome(options=chrome_options, executable_path=r'D:\Python\webdriver\chromedriver.exe')
driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
try:
    with open("D:/aaaaa.txt") as in_file:
        with open("D:/downloaded.txt", "w") as file:
          for url in in_file:
                driver.get(url.strip())
                time.sleep(5)
                driver.execute_script("window.print()")
                print('Printing ' + url + ' ' + str(i) + '/' + str_c)
                file.write(url)
                time.sleep(8)
                i = i+1
except:
    file.close()
    in_file.close()
    driver.close()



