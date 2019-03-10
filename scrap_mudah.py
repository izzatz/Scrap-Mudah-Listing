from bs4 import BeautifulSoup
#from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
import requests
import os, sys
import codecs

chromedriver_path = './chromedriver.exe'

homepage = "https://www.mudah.my/"
# url to search macbook in penang under category computer
url = "https://www.mudah.my/Penang/Computers-and-Accessories-3060/macbook-for-sale?lst=0&fs=1&w=103&cg=3060&q=macbook&so=1&st=s"
# url = "Used and New Laptops for sale, Buy second hand laptops in Malaysia, Sell laptops, computers, projectors, printers and hard disk drives in Malaysia.htm"

opts = ChromeOptions()
opts.add_experimental_option("detach", True)
driver = Chrome(chrome_options=opts)

keyword_search = "Macbook"

def nav_search_page():
    #driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
    driver.get(homepage)

    # click search button
    driver.find_element_by_class_name("btn-search").click()

    # click region
    driver.find_element_by_xpath("""//*[@id="findModal"]/div/div/div[2]/div/div/div[3]/a[1]""").click()

    # click category
    driver.find_element_by_xpath("""//*[@id="select2list-container-catgroup"]/ul/li[19]/a""").click()

    # search keyword in textbox
    driver.find_element_by_xpath("""//*[@id="searchtext"]""").text(keyword_search)



def extract_title():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all(lambda tag: tag.name == 'h2' and tag.get('class') == ['list_title'])

    for item in result:
        print (item)


def main():
    #extract_title()
    nav_search_page()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
	main()




