import test2
from main import *
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browse=webdriver.Chrome()
browse.implicitly_wait(5)

home=Home(browse)
log_page=home.go_to_login()
log_page.login(test2.my_login,test2.my_pass)
sleep(3)
log_page.search_tags("travel")
log_page.likey(2)

#
# browse.get("https://www.instagram.com/")

# user_input=browse.find_element_by_css_selector("input[name='username']")
# pass_input=browse.find_element_by_css_selector("input[name='password']")
# user_input.send_keys(test2.my_login)
# pass_input.send_keys(test2.my_pass)
# log_button=browse.find_element_by_css_selector("button[type='submit']")
# log_button.click()

#sleep(15)
#browse.close()