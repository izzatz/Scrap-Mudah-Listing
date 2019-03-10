from bs4 import BeautifulSoup
from selenium import webdriver
import requests
import os, sys
import codecs

# chromedriver_path = './chromedriver.exe'

# url to search macbook in penang under category computer
url = "https://www.mudah.my/Penang/Computers-and-Accessories-3060/macbook-for-sale?lst=0&fs=1&w=103&cg=3060&q=macbook&so=1&st=s"
# url = "Used and New Laptops for sale, Buy second hand laptops in Malaysia, Sell laptops, computers, projectors, printers and hard disk drives in Malaysia.htm"

# r = requests.get(url, headers=headers, proxies = proxies)

# driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
# driver.get(url)


def extract_title():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all(lambda tag: tag.name == 'h2' and tag.get('class') == ['list_title'])

    for item in result:
        print (item)


def main():
    extract_title()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
	main()




