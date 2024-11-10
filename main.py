import time
import random
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from fp.fp import FreeProxy
from Proxy_List_Scrapper import Scrapper, Proxy, ScrapperException
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.proxy import *

myProxy = "86.111.144.194:3128"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'ftpProxy': myProxy,
    'sslProxy': myProxy,
    'noProxy':''})

driver = webdriver.Chrome( proxy=)
driver.set_page_load_timeout(30)
driver.get('http://whatismyip.com')
time.sleep()
proxies = []
chrome_driver_path = 'cd/chromedriver.exe'
website_url = 'https://www.example.com'
import pytest
#
# from seleniumwire import webdriver
# # In order for pytest to recognise the test, the test name must begin with test_&lt;name> (for example, test_lambdatest_todo_app).
# def test_case():
#     chrome_options = Options()
#     #     chrome_options.add_argument(f"--proxy-server={proxy}")
#     driver = webdriver.Chrome(se)
#     driver.maximize_window()
#     driver.get("https://ecommerce-playground.lambdatest.io/")
#     search_for_key = driver.find_element(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div[2]/input')
#     search_for_key.send_keys("iphone")
#     search_btn = driver.find_element(By.XPATH,'//*[@id="search"]/div[2]/button')
#     search_btn.click()
#     time.sleep(30)
#     driver.close()

# def proxy_list():
#     scrapper = Scrapper(category='ALL', print_err_trace=False)
#     data = scrapper.getProxies()
#     for item in data.proxies[:10]:
#         proxies.append('{}:{}'.format(item.ip, item.port))
#
#     print("Proxy List: {}".format(proxies))
#
#
# def proxy_data(name):
#     proxy = FreeProxy(rand=True).get(10)
#
#     print(proxy)
#
#
# def browsers_open():
#     proxy = random.choice(proxies)
#     # proxy = FreeProxy(rand=True).get()
#     print(proxy)
#     chrome_options = Options()
#     chrome_options.add_argument(f"--proxy-server={proxy}")
#     # chrome_options.add_argument("--headless")
#     service = Service(chrome_driver_path)
#     driver = webdriver.Chrome(service=service, options=chrome_options)
#     try:
#         driver.get(website_url)
#     except WebDriverException:
#         print("page down")
#
#
#     # Open the website with the selected proxy
#     # driver.get(website_url)
#     # Wait for 30 seconds
#     # time.sleep(10)
#     # try:
#     #     button = driver.find_element(By.ID, 'someButtonID')  # Replace with actual button ID
#     #     button.click()
#     #     time.sleep(2)
#     # except Exception as e:
#     #     print(f"Error occurred: {e}")
#
#     # You can simulate scrolling or other interactions as needed
#     # Close the current tab
#     # driver.close()
#
#     # If it's the last loop, we need to open a new instance to restart the process
#     # driver = webdriver.Chrome(service=service, options=chrome_options)
#     # driver.quit()
#
#
# if __name__ == '__main__':
#     proxy_list()
#     browsers_open()
