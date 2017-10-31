# Import the necessary module
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from config import url, utc_datetimenow, nama, username, password, cfmPassword, dob, gender, handphone

# Instantiate the webdriver class
driver = webdriver.Chrome()
# Implicitly wait for 3 seconds
driver.implicitly_wait(3)
# Call the url
driver.get(url)

# Find element based on name, then enter the keys
el_nama = driver.find_element_by_name("nama")
el_nama.clear()
el_nama.send_keys(nama)

el_username = driver.find_element_by_name("username")
el_username.clear()
el_username.send_keys(username)
print(username)

el_password = driver.find_element_by_name("password")
el_password.clear()
el_password.send_keys(password)

el_cfmPassword = driver.find_element_by_name("cfmPassword")
el_cfmPassword.clear()
el_cfmPassword.send_keys(cfmPassword)

el_dob = driver.find_element_by_name("dob")
el_dob.clear()
el_dob.send_keys(dob)

# Find element based on name, instantiate Select class, then change the option value
el_gender = driver.find_element_by_name("gender")
select = Select(el_gender)
select.select_by_value(gender)

el_handphone = driver.find_element_by_name("handphone")
el_handphone.clear()
el_handphone.send_keys(handphone)

# Find element based on name, then click the element
el_tou = driver.find_element_by_name("tou")
el_tou.click()
el_tou.send_keys(u'\ue007')

driver.close()
