from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.chrome.service as service
import time

url = "https://api.whatsapp.com/send?phone=918299246532&text=hello"
options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=E:\Main()\work\Anchor\Anchor 0.0\Profiles\Profile 9")
driver = webdriver.Chrome(options=options,
                                          executable_path="E:\Main()\work\Anchor\Anchor 0.05\chromedrivers\chromedriver5.exe")
driver.get(url)
time.sleep(10030)
driver.close()

