from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import urllib
import requests
import os
import codecs
import smtplib
import time

# chromedriver binary path
chromedriver_path = './chromedriver.exe'

# caps setting for page loading settings
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  # complete
# caps["pageLoadStrategy"] = "eager"  #interactive
# caps["pageLoadStrategy"] = "none"

# Chrome options
opts = ChromeOptions()
opts.add_experimental_option("detach", True)

headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/53.0.2785.143 Safari/537.36'}
set_proxies = {'http': 'http://proxy.kssm.intel.com:911',
               'https': 'http://proxy.kssm.intel.com:911'}

proxies = None  # put None to disable proxy / put proxies = set_proxies to enable

# driver = Chrome(options=opts, desired_capabilities=caps)

# url of the homepage that will be scrap
homepage = "https://www.mudah.my/"

# url to search macbook in penang under category computer
url = "https://www.mudah.my/Penang/Computers-and-Accessories-3060/macbook-for-sale?lst=0&fs=1&w=103&cg=3060&q=macbook&so=1&st=s"
offline_url = "C:\\Users\\Izzatz-X240\\Desktop\\Github\\Scrap-Mudah-Listing\\Scrap-Mudah-Listing\\offline_pages\\Used and New Laptops for sale, Buy second hand laptops in Malaysia, Sell laptops, computers, projectors, printers and hard disk drives in Malaysia.html"
# global keyword search can be set here
keyword_search = "Macbook"

result_list = []
#result_list = result_list_offline
#result_list_offline = ["""[<h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015+i5+256GB-76948908.htm" title=" Macbook Air 13 ,2015, i5 256GB">Macbook Air 13 ,2015, i5 256GB</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro+13-77476029.htm" title=" Macbook pro 13">Macbook pro 13</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro-77460794.htm" title=" Macbook Pro">Macbook Pro</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro+13inc+mid2012+-77458827.htm" title=" Macbook pro (13inc mid2012)">Macbook pro (13inc mid2012)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Mini+DisplayPort+to+VGA+Adapter-73550042.htm" title=" Macbook Mini DisplayPort to VGA Adapter">Macbook Mini DisplayPort to VGA Adapter</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro+250gb+2017-77364045.htm" title=" Macbook pro 250gb 2017">Macbook pro 250gb 2017</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/13+3inch+MacBook+Pro+Retina+2013+year-77311279.htm" title=" 13.3inch MacBook Pro Retina 2013 year">13.3inch MacBook Pro Retina 2013 year</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air-77269772.htm" title=" MacBook Air">MacBook Air</a></h2>, <h2 class="list_title"><a bag"="" folder="" href="https://www.mudah.my/Apple+MacBook+Pro+15+4+Folder+Bag-77267102.htm" title=" Apple MacBook Pro 15.4">Apple MacBook Pro 15.4" Folder Bag</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+12+8gb+256gb+new+battery+CAN+TRADE+-77253042.htm" title=" Macbook 12 8gb 256gb new battery (CAN TRADE)">Macbook 12 8gb 256gb new battery (CAN TRADE)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Pro-74234302.htm" title=" MacBook Pro">MacBook Pro</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015+90+New+-76802993.htm" title=" Macbook Air 13 ,2015 (90% New)">Macbook Air 13 ,2015 (90% New)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Brand+And+Model+Macbook+Pro+13+2011+i5+240GB+SS-76718061.htm" title=" Brand And Model: Macbook Pro 13 ,2011, i5 240GB SS">Brand And Model: Macbook Pro 13 ,2011, i5 240GB SS</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+Retina+15+2013+Late+i7+256GB+SSD-76925126.htm" title=" Macbook Pro Retina 15 ,2013 Late, i7, 256GB SSD">Macbook Pro Retina 15 ,2013 Late, i7, 256GB SSD</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Apple+MacBook+Pro+Touch+Bar+8ram+256gb-76885447.htm" title=" Apple MacBook Pro Touch Bar 8ram 256gb">Apple MacBook Pro Touch Bar 8ram 256gb</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+15+inch+mid+2014+16GB+512GB+SSD-76880606.htm" title=" Macbook Pro 15 inch mid 2014 16GB 512GB SSD">Macbook Pro 15 inch mid 2014 16GB 512GB SSD</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Apple+Macbook+60W+Magsafe+Power+Adapter-76865032.htm" title=" Apple Macbook 60W Magsafe Power Adapter">Apple Macbook 60W Magsafe Power Adapter</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+air+11inch+late+2011-76800143.htm" title=" Macbook air 11inch late 2011">Macbook air 11inch late 2011</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Laptop+apple+macbook+air+intel+core+i5-76779877.htm" title=" Laptop apple macbook air intel core i5">Laptop apple macbook air intel core i5</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+12+inch+2016-76725133.htm" title=" Macbook 12 inch 2016">Macbook 12 inch 2016</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015+256GB-76414370.htm" title=" Macbook Air 13 ,2015, 256GB">Macbook Air 13 ,2015, 256GB</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+apple+Mini+DisplayPort+to+VGA+Adapter-73304027.htm" title=" Macbook apple Mini DisplayPort to VGA Adapter">Macbook apple Mini DisplayPort to VGA Adapter</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+11+inch-76545242.htm" title=" Macbook Air 11-inch">Macbook Air 11-inch</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Pro+13+inch+Mid+2010+-76442533.htm" title=" MacBook Pro 13 inch (Mid 2010)">MacBook Pro 13 inch (Mid 2010)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13inch-76436171.htm" title=" Macbook Air 13inch">Macbook Air 13inch</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+13+A1278+Clear+Screen+Protector-76388211.htm" title=" Macbook Pro 13 A1278 Clear Screen Protector">Macbook Pro 13 A1278 Clear Screen Protector</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+inch+Mid+2012-73500797.htm" title=" Macbook Air 13 inch Mid 2012">Macbook Air 13 inch Mid 2012</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Pro+A1278+Case+and+keyboard+protector-76350958.htm" title=" MacBook Pro A1278 Case and keyboard protector">MacBook Pro A1278 Case and keyboard protector</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+air-76288603.htm" title=" Macbook air">Macbook air</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air-76286648.htm" title=" MacBook Air">MacBook Air</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Core2Duo+4GB+RAM-76280342.htm" title=" MacBook Core2Duo 4GB RAM">MacBook Core2Duo 4GB RAM</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air+LIKE+NEW-76241021.htm" title=" MacBook Air LIKE NEW">MacBook Air LIKE NEW</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air+13+3+inch+8GB+RAM+256GB+STORAGE-76234860.htm" title=" MacBook Air 13.3 inch 8GB RAM 256GB STORAGE">MacBook Air 13.3 inch 8GB RAM 256GB STORAGE</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air-76195496.htm" title=" MacBook Air">MacBook Air</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+air+11inch-76176021.htm" title=" Macbook air 11inch">Macbook air 11inch</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+12+2016-76141663.htm" title=" Macbook 12 2016">Macbook 12 2016</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+Retina+2018+Model+Warranty-75998735.htm?last=1" title=" Macbook Air Retina , 2018 Model,Warranty">Macbook Air Retina , 2018 Model,Warranty</a></h2>]"""]

url_list = []
result_dict = {}

# global var to store empty string. Later will overwrite with a password that being read from a txt file.
gmail_app_password = ""


def check_website_up_down():
    proxy_support = urllib.request.ProxyHandler(proxies)
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    if (urllib.request.urlopen(homepage).getcode()) == 200:
        # print("True")
        return True
    else:
        # print("False")
        return False


def nav_search_page():
    # driver = webdriver.Chrome(chromedriver_path)  # Optional argument, if not specified will search path.
    driver.get(homepage)

    # click search button
    driver.find_element_by_class_name("btn-search").click()

    # click region
    driver.find_element_by_xpath(
        """//*[@id="findModal"]/div/div/div[2]/div/div/div[3]/a[1]""").click()

    # click category
    # driver.find_element_by_xpath("""//*[@id="select2list-button-catgroup"]""").click()
    # time.sleep(3)
    # driver.find_element_by_xpath("""// *[ @ id = "catgroup"] / option[23]""").click()

    # search keyword in textbox
    # driver.find_element_by_xpath("""//*[@id="searchtext"]""").text(keyword_search)


def next_page_availability():
    # try catch block to check for next page availability
    try:
        # find next page button
        driver.find_element_by_xpath(
            """// *[ @ id = "list_ads_container"] / div[2] / div[3] / span[2] / span / a""")

    except NoSuchElementException:
        return False
        # print("Not found")

    else:
        return True
        # driver.find_element_by_xpath("""// *[ @ id = "list_ads_container"] / div[2] / div[3] / span[2] / span / a""").click()
        # extract_title()


def check_next_page():
    while next_page_availability() == True:
        extract_title()
    else:
        list_href_only()


def start_page():  # automatically start with shortcut links, start with my preferred location Penang and category that I'm working on.
    driver.get(url)


def extract_title():
    page = requests.get(url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(page.content, 'html.parser')
    print(soup.title)
    result = soup.find_all(lambda tag: tag.name ==
                           'h2' and tag.get('class') == ['list_title'])
    result_list.extend(result)
    # print(result)


def list_href_only():  # print links only
    print("Total items: ", (len(result_list)))
    # print(result_list)
    for item_list in result_list:
        # Find the url on each line
        for a in item_list('a', href=True):
            a_url = a['href']
            # print (a_url)
            url_list.append(a_url)

    # print the global url_list
    for line in url_list:
        print(line)


def list_title_only():
    print("Total items: ", (len(result_list)))
    for each_tag in result_list:
        staininfo_attrb_value = each_tag["title"]
        print(staininfo_attrb_value)


def read_gmail_pass():  # func to read a txt file that contain a gmail app password.
    file_pass = open("pass.txt", "r")
    # print(f.read())
    temp_password = (file_pass.read())
    global gmail_app_password
    gmail_app_password = temp_password
    # print(gmail_app_password)


def send_email():
    read_gmail_pass()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('iz.mail.robot@gmail.com', gmail_app_password)

    subject = 'New iPhone Listing!'
    body = 'Check the iPhone Listing'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'iz.mail.robot@gmail.com',
        'izzatz13@gmail.com',
        msg
    )

    print('Email has been sent')

    server.quit()


def main():
    # start_page()
    extract_title()
    list_href_only()
    # list_title_only()
    # if check_website_up_down() == True:
    #     print("Website is up!\n")
    #     start_page()
    #     extract_title()
    #     list_href_only()

    # else:
    #     print("Website is down!")

    # nav_search_page()
    # start_page()
    # next_page_availability()
    # check_next_page()
    # extract_title()
    # list_href_only()
    # send_email()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
