import os
import shutil
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.options import Options
import time

from secret import username, password

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)

# elem1 = waiting.until(EC.element_to_be_clickable(('id','email')))
time.sleep(4)
email = driver.find_element_by_id('email')
email.send_keys(username)
time.sleep(1)
pw = driver.find_element_by_id('password')
pw.send_keys(password)
time.sleep(1)
login = driver.find_element_by_xpath('//*[@id="signIn"]/form/div[3]/div[2]/button')
login.click()
time.sleep(3)
bob = driver.find_element_by_xpath('//*[@id="retentionLink"]/div/button[1]')
bob.click()
time.sleep(3)
client_list = []
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.findAll('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r")
    title = title.strip(" \n")
    client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.findAll('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r")
    title = title.strip(" \n")
    if title not in client_list:
        client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.findAll('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r")
    title = title.strip(" \n")
    if title not in client_list:
        client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.findAll('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
    if title not in client_list:
        client_list.append(title)
time.sleep(1)
print("There are " + str(len(client_list)) + " clients.")
time.sleep(2)
print(client_list)

# client_set = set(client_list)
# print(client_set)
# num_clients = len(client_set_list)
# print("There are " + str(num_clients) + " clients.")



# images = []
# for i in sel_soup.findAll("img"):
#     src = i["src"]
#     images.append(src)
# print(images)
# current_path = os.getcwd()
# for img in images:
#     try:
#         file_name = os.path.basename(img)
#         img_r = requests.get(img, stream=True)
#         new_path = os.path.join(current_path, "images", file_name)
#         with open(new_path, "wb") as output_file:
#             shutil.copyfileobj(img_r.raw, output_file)
#         del img_r
#     except:
#         pass

# iterations = 0
# while iterations < 10:
#     html = driver.execute_script("return document.documentElement.outerHTML")
#     sel_soup = BeautifulSoup(html, 'html.parser')
#     print(len(sel_soup.findAll("img")))
#     images = []
#     for i in sel_soup.findAll("img"):
#         src = i["src"]
#         images.append(src)
#     print(images)
#     current_path = os.getcwd()
#     for img in images:
#         try:
#             file_name = os.path.basename(img)
#             img_r = requests.get(img, stream=True)
#             new_path = os.path.join(current_path, "images", file_name)
#             with open(new_path, "wb") as output_file:
#                 shutil.copyfileobj(img_r.raw, output_file)
#             del img_r
#         except:
#             pass
#     iterations += 1
#     time.sleep(5)