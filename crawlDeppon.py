import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="./chromedriver")
driver.get("https://www.deppon.com/deptlist/")
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
items = soup.select('div[class~="listA_Z"] a')
for item in items:
    print(item.string)

