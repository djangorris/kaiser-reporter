import os
import os.path
from selenium import webdriver

from functions import (
	old_file_csv_to_list,
	kaiser_login,
	initialize_list,
	scroll_add_new_to_list,
	create_newFile,
	send_the_email,
	)

if os.path.isfile("new_file.csv"):
	os.rename("new_file.csv", "old_file.csv")

old_list = old_file_csv_to_list()
old_num_clients = len(old_list)

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)

kaiser_login(driver)

new_list = []

initialize_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

new_num_clients = len(new_list)

create_newFile(new_list)

# number difference b/w old_num_clients & new_num_clients as num_client_difference

# make list of added or removed clients

# use variation of compare.py to show added and removed clients

# LAST FEATURE: count the total number of clients by accessing the number of/
# family members 

send_the_email(old_list, old_num_clients, new_list, new_num_clients)
