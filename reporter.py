from selenium import webdriver

from functions import (
	kaiser_login,
	initialize_list,
	scroll_add_new_to_list,
	create_newFile,
	send_the_email,
	)

os.rename("new_file.csv", "old_file.csv")

# bring in old list as old_list

# set len(old_list) to old_num_clients

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

send_the_email(new_list, new_num_clients)
