#to unfollow given list of peeps
import sys
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys


text_file = sys.argv[1]
text_file = open(text_file, "r") 
lines = text_file.read().split('\n')


driver = webdriver.Chrome(sys.argv[4])

driver.get('https://www.instagram.com/accounts/login/')
sleep(10)
id_box_name = driver.find_element_by_name('username')
id_box_name.send_keys(sys.argv[2])
id_box_pass = driver.find_element_by_name('password')
id_box_pass.send_keys(sys.argv[3])
id_box_pass.send_keys(Keys.ENTER)
sleep(5)

for name in lines:
	driver.get('https://www.instagram.com/'+name+'/')
	sleep(5)
	unfollow_button = driver.find_element_by_class_name("BY3EC.sqdOP.L3NKy._8A5w5")
	unfollow_button.click()
	sleep(2)
	driver.find_element_by_class_name("aOOlW.-Cab_").click() 
	print("Unfollowed " + name + ".")
	sleep(2)
