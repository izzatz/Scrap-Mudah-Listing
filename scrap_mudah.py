from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import codecs

# chromedriver_path = './chromedriver.exe'

# url to search macbook in penang under category computer
url = "https://www.mudah.my/Penang/Computers-and-Accessories-3060/macbook-for-sale?lst=0&fs=1&w=103&cg=3060&q=macbook&so=1&st=s"


# proxy settings
# proxies = {'http':'http://proxy.kssm.intel.com:911', 'https':'http://proxy.kssm.intel.com:911'}
# r = requests.get(url, headers=headers, proxies = proxies)

# driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
# driver.get(url)


page = requests.get(url)

# print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

# with open("out.log", "w") as file:
#    file.write(str(soup))

