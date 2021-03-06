import csv
import os
import shutil
import smtplib
import time
from bs4 import BeautifulSoup
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
from smtplib import SMTP, SMTPAuthenticationError, SMTPException

from secret import kaiser_username, kaiser_password, host, port, username, password, from_email, to_list
from templates import get_template_path, get_template, render_context
	

def old_file_csv_to_list():
    with open('old_file.csv', 'r') as f:
        return f.read().splitlines()

def kaiser_login(driver):
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

def initialize_list(driver, new_list):
	html = driver.execute_script("return document.documentElement.outerHTML")
	sel_soup = BeautifulSoup(html, 'html.parser')
	clients = sel_soup.find_all("div", class_="name")
	for client in clients:
	    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
	    new_list.append(title)

def scroll_add_new_to_list(driver, new_list):
	time.sleep(1)
	driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
	html = driver.execute_script("return document.documentElement.outerHTML")
	sel_soup = BeautifulSoup(html, 'html.parser')
	clients = sel_soup.find_all("div", class_="name")
	for client in clients:
	    title = client.find_all('a', {'class': 'ng-binding'})[0].text.strip(" /n/t/r\n")
	    if title not in new_list:
	        new_list.append(title)

# def added_clients(old_list, new_list):
# 	return set(new_list) - set(old_list)

# def removed_clients(old_list, new_list):
# 	return (set(old_list) or set(new_list)) - set(new_list)

def create_newFile(new_list):
    with open("new_file.csv", 'w') as newFile:
        newFile.write('\n'.join(new_list))

def send_the_email(old_list, old_num_clients, new_list, new_num_clients, added, removed):
	# try:
	email_conn = smtplib.SMTP(host, port)
	email_conn.ehlo()
	email_conn.starttls()
	email_conn.login(username, password)
	the_msg = MIMEMultipart('alternative')
	the_msg['Subject'] = "Kaiser client update"
	the_msg['From'] = from_email

	file_ = 'templates/email_message.txt'
	file_html = 'templates/email_message.html'
	template = get_template(file_)
	template_html = get_template(file_html)
	context = {
		"old_num_clients": old_num_clients,
	    "old_list": old_list,
	    "new_num_clients": new_num_clients,
	    "new_list": new_list,
	    "added": added,
	    "removed": removed,
	}
	rendered_text = render_context(template, context)
	rendered_html = render_context(template_html, context)
	part_1 = MIMEText(rendered_text, 'plain')
	part_2 = MIMEText(rendered_html, "html")
	the_msg.attach(part_1)
	the_msg.attach(part_2)
	email_conn.sendmail(from_email, to_list, the_msg.as_string())
	email_conn.quit()
	# except smtplib.SMTPException:
	#     print("error sending message")