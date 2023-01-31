import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pprint import pprint
import time


MIN_price = 200000
MAX_price = 800000

city = input(
    'Enter city to get price, addreess and links to the properties in that city: ')

URL = f'https://www.zolo.ca/{city}-real-estate'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

# ***************************************************TODO GET PROPERTY PRICES*******************************

property_price = soup.find_all(
    "li", class_='price xs-block xs-mb1 text-2 heavy')
property_price_list = []
for i in range(len(property_price)):

    property_price_list.append(property_price[i].text)

# print(property_price_list)

# ***************************************************TODO GET PROPERTY ADDRESSESS*******************************

property_address = soup.find_all(
    "h3", class_='card-listing--location text-5 xs-inline')
property_address_list = []

for i in range(len(property_address)):

    property_address_list.append(property_address[i].text)

# print(property_address_list)

# ***************************************************TODO GET PROPERTY LINKS*******************************

property_link = soup.find_all(
    "a", class_='address text-primary')
property_link_list = []

for i in range(len(property_link)):

    property_link_list.append(property_link[i].get('href'))

# print(property_link_list)

""" final = {}
result = []
for price in range(len(property_price_list)):
    if property_price_list[price] >= MIN_price and property_price_list[price] <= MAX_price:

        final = {price: {"property price": property_price_list[price],
                         'property address': property_address_list[price], 'property link': property_link_list[price]}}

    result.append(final)

# print(result) """


for i in range(len(property_price_list)):
    chrome_driver_path = "C:/Development/chromedriver.exe"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)

    driver = webdriver.Chrome(options=options, service=Service(
        executable_path=chrome_driver_path, log_path="NUL"))
    driver.maximize_window()
    driver.get("https://forms.gle/41GnpNkZccnaXTxx7")
    driver.implicitly_wait(10)

    time.sleep(2)
    send_property_address = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_property_address.send_keys(property_address_list[i])

    send_property_price = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_property_price.send_keys(property_price_list[i])

    send_property_link = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    send_property_link.send_keys(property_link_list[i])

    submit_btn = driver.find_element(
        By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    submit_btn.click()
    driver.quit()
