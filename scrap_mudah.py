from bs4 import BeautifulSoup
from selenium.webdriver import ChromeOptions, Chrome
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException
import requests, time, os, sys, codecs

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
result_list = []
#result_list = ["""<h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13inches+i5+8gb+128gb+Bought+2016+-73734059.htm" title=" Macbook Air 13inches i5/8gb/128gb(Bought 2016)">Macbook Air 13inches i5/8gb/128gb(Bought 2016)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015-73482380.htm" title=" Macbook Air 13 ,2015">Macbook Air 13 ,2015</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/DDR3+2GB+RAM+MacBook+-72235728.htm" title=" DDR3 2GB RAM (MacBook)">DDR3 2GB RAM (MacBook)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2014-73692336.htm" title=" Macbook Air 13 ,2014">Macbook Air 13 ,2014</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+13+2011+Model-72988448.htm" title=" Macbook Pro 13 ,2011 Model">Macbook Pro 13 ,2011 Model</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+apple+Mini+DisplayPort+to+VGA+Adapter-73304027.htm" title=" Macbook apple Mini DisplayPort to VGA Adapter">Macbook apple Mini DisplayPort to VGA Adapter</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Apple+MacBook+Pro+2010+4GB+Nvidia+GeForce+13a+-73640967.htm" title=" Apple MacBook Pro 2010 /4GB/Nvidia GeForce/13”">Apple MacBook Pro 2010 /4GB/Nvidia GeForce/13”</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro+A1278+core+2+duo+nvidia+geforce-73640941.htm" title=" Macbook pro A1278, core 2 duo, nvidia geforce">Macbook pro A1278, core 2 duo, nvidia geforce</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+12+inch+256GB+Early+2015+-73640670.htm" title=" Macbook 12 inch 256GB (Early 2015)">Macbook 12 inch 256GB (Early 2015)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Pro+Retina+13+inch+Late+2013-73587077.htm" title=" MacBook Pro Retina 13-inch Late 2013">MacBook Pro Retina 13-inch Late 2013</a></h2>, <h2 class="list_title"><a 2014"="" href="https://www.mudah.my/Macbook+Air+11+2014-73563837.htm" title=" Macbook Air 11">Macbook Air 11" 2014</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+11+2015-73330941.htm" title=" Macbook Air 11 ,2015">Macbook Air 11 ,2015</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+13-73053453.htm" title=" Macbook Pro 13">Macbook Pro 13</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Mini+DisplayPort+to+VGA+Adapter-73550042.htm" title=" Macbook Mini DisplayPort to VGA Adapter">Macbook Mini DisplayPort to VGA Adapter</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+256GB+SSD+2014-73530940.htm" title=" Macbook Air 13 ,256GB SSD, 2014">Macbook Air 13 ,256GB SSD, 2014</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+11+2014-73512364.htm" title=" Macbook Air 11 ,2014">Macbook Air 11 ,2014</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+inch+Mid+2012-73500797.htm" title=" Macbook Air 13 inch Mid 2012">Macbook Air 13 inch Mid 2012</a></h2>, <h2 class="list_title"><a (mid-2012)"="" href="https://www.mudah.my/MacBook+Pro+13+Mid+2012+-73483133.htm" title=" MacBook Pro 13">MacBook Pro 13" (Mid-2012)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro-73364986.htm" title=" Macbook pro">Macbook pro</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+Retina+13+2014-73454777.htm" title=" Macbook Pro Retina 13 ,2014">Macbook Pro Retina 13 ,2014</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/2017+MacBook+Air+13+inch+256SSD-73402558.htm" title=" 2017 MacBook Air 13-inch 256SSD">2017 MacBook Air 13-inch 256SSD</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+pro-73399655.htm" title=" Macbook pro">Macbook pro</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+Retina+13+2014+256GB+SSD-73399149.htm" title=" Macbook Pro Retina 13 ,2014, 256GB SSD">Macbook Pro Retina 13 ,2014, 256GB SSD</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Pro-73397404.htm" title=" MacBook Pro">MacBook Pro</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2017+Warranty-73375804.htm" title=" Macbook Air 13 ,2017 ,Warranty">Macbook Air 13 ,2017 ,Warranty</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+2018+Used+1+2+year+4+5y+warranty-73354272.htm" title=" Macbook Pro  2018 (Used 1/2 year) 4.5y warranty">Macbook Pro  2018 (Used 1/2 year) 4.5y warranty</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+Retina+13+2015-73353239.htm" title=" Macbook Pro Retina 13 ,2015">Macbook Pro Retina 13 ,2015</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+15+i7+8GB+Ram-73330924.htm" title=" Macbook Pro 15, i7,8GB Ram">Macbook Pro 15, i7,8GB Ram</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook-73306534.htm" title=" Macbook">Macbook</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+Early+2015-73239582.htm" title=" Macbook Air 13 Early 2015">Macbook Air 13 Early 2015</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/MacBook+Air+11+2015+i5+256SSD+4GB+RAM-73135339.htm" title=" MacBook Air 11' 2015 i5 256SSD 4GB RAM">MacBook Air 11' 2015 i5 256SSD 4GB RAM</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+air-73126567.htm" title=" Macbook air">Macbook air</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015+Model+90+New+-73079302.htm" title=" Macbook Air 13 ,2015 Model (90% New)">Macbook Air 13 ,2015 Model (90% New)</a></h2>, <h2 class="list_title"><a 2.5gb"="" 2013="" 512ssd="" graphic="" href="https://www.mudah.my/Macbook+Pro+15+Late+2013+512SSD+Graphic+2+5GB-72891246.htm" late="" title=" Macbook Pro 15">Macbook Pro 15" Late 2013 512SSD Graphic 2.5GB</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Pro+13+2010+Model+New+Battery-72956955.htm" title=" Macbook Pro 13, 2010 Model, New Battery">Macbook Pro 13, 2010 Model, New Battery</a></h2>, <h2 class="list_title"><a "="" href="https://www.mudah.my/Macbook+Pro+13+-72926400.htm" title=" Macbook Pro 13">Macbook Pro 13"</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+2015+128SSD+Silver+Can+Swap+-72804958.htm" title=" Macbook Air 13 2015 128SSD Silver (Can Swap)">Macbook Air 13 2015 128SSD Silver (Can Swap)</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+13+i5+256GB+SSD-72800503.htm" title=" Macbook Air 13,i5,256GB SSD">Macbook Air 13,i5,256GB SSD</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+12+Retina+256GB+SSD+Full+Set-72783239.htm" title=" Macbook 12 Retina,256GB SSD Full Set">Macbook 12 Retina,256GB SSD Full Set</a></h2>, <h2 class="list_title"><a href="https://www.mudah.my/Macbook+Air+11+i5+256GB+SSD-72770436.htm" title=" Macbook Air 11, i5,256GB SSD">Macbook Air 11, i5,256GB SSD</a></h2>"""]

result_dict = {}


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
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'}

    proxies = {'http': 'http://proxy.kssm.intel.com:911', 'https': 'http://proxy.kssm.intel.com:911'}
    page = requests.get(url, headers=headers, proxies=proxies)
    #page = requests.get(url, headers=headers)

    #page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    result = soup.find_all(lambda tag: tag.name == 'h2' and tag.get('class') == ['list_title'])
    # print (result)
    result_list.extend(result)


def list_all():
    print("Total items: ", (len(result_list)))
    for item_list in result_list:
        # Find the url on each line
        for a in item_list('a', href=True):
            print ("Found the URL:", a['href'])    
        # print(item_list)


def process_dict():
    # Process previous list result and convert it to dictionary
    # result_list
    print("Started list conversion to dictionary")
    

def main():
    # nav_search_page()
    start_page()
    #next_page()
    extract_title()
    list_all()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
	main()