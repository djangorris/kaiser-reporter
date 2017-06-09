import os
import shutil
import requests
from selenium import webdriver
import time

from functions import scroll_add_new_to_list, kaiser_login, initialize_list, send_the_email

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)
time.sleep(4)

kaiser_login(driver)

# bring in old list as old_list
# set len(old_list) to old_num_clients
# change client_list (below) to new_list
client_list = []

initialize_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

scroll_add_new_to_list(driver, client_list)

# change to new_num_clients
num_clients = len(client_list)
# number difference b/w old_num_clients & new_num_clients as num_client_difference
# make list of added or removed clients
# count the total number of clients by accessing the number of/
# family members 

send_the_email(client_list, num_clients)
