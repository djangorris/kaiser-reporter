from selenium import webdriver

from functions import scroll_add_new_to_list, kaiser_login, initialize_list, send_the_email

url = "https://clear.kaiserpermanente.org/?kp_shortcut_referrer=kp.org/clear#/login"
driver = webdriver.Firefox()
driver.get(url)

kaiser_login(driver)

# bring in old list as old_list

# set len(old_list) to old_num_clients

new_list = []

initialize_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

scroll_add_new_to_list(driver, new_list)

# change to new_num_clients
num_clients = len(new_list)
# number difference b/w old_num_clients & new_num_clients as num_client_difference
# make list of added or removed clients
# count the total number of clients by accessing the number of/
# family members 

send_the_email(new_list, num_clients)
