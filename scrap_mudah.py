from bs4 import BeautifulSoup
#from selenium import webdriver
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import requests
import time
import os, sys
import codecs

# chromedriver binary path
chromedriver_path = './chromedriver.exe'

# caps setting for page loading settings
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #complete
#caps["pageLoadStrategy"] = "eager"  #interactive
#caps["pageLoadStrategy"] = "none"

# Chrome options
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

driver = Chrome(options=opts, desired_capabilities=caps)

# url of the homepage that will be scrap
homepage = "https://www.mudah.my/"

# url to search macbook in penang under category computer
url = "https://www.mudah.my/Penang/Computers-and-Accessories-3060/macbook-for-sale?lst=0&fs=1&w=103&cg=3060&q=macbook&so=1&st=s"

# global keyword can be set here
keyword_search = "Macbook"

result_list = result


def nav_search_page():
    #driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
    driver.get(homepage)

    # click search button
    driver.find_element_by_class_name("btn-search").click()

    # click region
    driver.find_element_by_xpath("""//*[@id="findModal"]/div/div/div[2]/div/div/div[3]/a[1]""").click()

    # click category
    # driver.find_element_by_xpath("""//*[@id="select2list-button-catgroup"]""").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("""// *[ @ id = "catgroup"] / option[23]""").click()


    # search keyword in textbox
    #driver.find_element_by_xpath("""//*[@id="searchtext"]""").text(keyword_search)

def start_page():
    # automatically start with shortcut links, start with my preferred location Penang and category that I'm working on.
    driver.get(url)
    print(result_list)


def next_page():
    # try catch block to check for next page availability
    try:
        # find next page button
        driver.find_element_by_xpath("""// *[ @ id = "list_ads_container"] / div[2] / div[3] / span[2] / span / a""")
    except NoSuchElementException:
        print("Not found")
    else:
        print("Found")


def extract_title():
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all(lambda tag: tag.name == 'h2' and tag.get('class') == ['list_title'])

    return result

    # print(len(result))
    # for item in result:
    #     print(item)


def list_all(result):
    result = result_list
    print(len(result_list))
    for item_list in result_list:
        print(item_list)

def main():
    #extract_title()
    # nav_search_page()
    start_page()
    #next_page()
    extract_title()
    list_all()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
	main()




