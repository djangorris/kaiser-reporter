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
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from smtplib import SMTP, SMTPAuthenticationError, SMTPException
import time

from secret import kaiser_username, kaiser_password, host, port, username, password, from_email, to_list
from templates import get_template_path, get_template, render_context

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)

# elem1 = waiting.until(EC.element_to_be_clickable(('id','email')))
time.sleep(4)
email = driver.find_element_by_id('email')
email.send_keys(kaiser_username)
time.sleep(1)
pw = driver.find_element_by_id('password')
pw.send_keys(kaiser_password)
time.sleep(1)
login = driver.find_element_by_xpath('//*[@id="signIn"]/form/div[3]/div[2]/button')
login.click()
time.sleep(4)
bob = driver.find_element_by_xpath('//*[@id="retentionLink"]/div/button[1]')
bob.click()
time.sleep(3)
client_list = []
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
    client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
    if title not in client_list:
        client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
    if title not in client_list:
        client_list.append(title)
time.sleep(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html, 'html.parser')
clients = sel_soup.find_all("div", class_="name")
for client in clients:
    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
    if title not in client_list:
        client_list.append(title)
num_clients = len(client_list)
# print("There are {} families.".format(num_clients))
# print(client_list)

# try:
email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username, password)
the_msg = MIMEMultipart('alternative')
the_msg['Subject'] = "Kaiser client update"
the_msg['From'] = from_email

###
file_ = 'templates/email_message.txt'
file_html = 'templates/email_message.html'
template = get_template(file_)
template_html = get_template(file_html)
context = {
    "num_clients": num_clients,
    "client_list": client_list,
}

rendered_text = render_context(template, context)
rendered_html = render_context(template_html, context)

part_1 = MIMEText(rendered_text, 'plain')
part_2 = MIMEText(rendered_html, "html")
the_msg.attach(part_1)
the_msg.attach(part_2)
# the_msg = render_context(template, context)
# the_msg = render_context(template_html, context)
email_conn.sendmail(from_email, to_list, the_msg.as_string())
email_conn.quit()
# except smtplib.SMTPException:
#     print("error sending message")