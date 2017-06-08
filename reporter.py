import os
import shutil
import requests
from selenium import webdriver
import time

from functions import scroll_add_new_to_list, kaiser_login, initialize_list, email_list

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)

kaiser_login(driver)

client_list = []

initialize_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

num_clients = len(client_list)

email_list(client_list, num_clients)
