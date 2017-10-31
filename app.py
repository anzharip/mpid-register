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
elem = driver.find_element_by_name("nama")
elem.clear()
elem.send_keys(nama)

elem = driver.find_element_by_name("username")
elem.clear()
elem.send_keys(username)
print(username)

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys(password)

elem = driver.find_element_by_name("cfmPassword")
elem.clear()
elem.send_keys(cfmPassword)

elem = driver.find_element_by_name("dob")
elem.clear()
elem.send_keys(dob)

# Find element based on name, instantiate Select class, then change the option value
elem = driver.find_element_by_name("gender")
select = Select(elem)
select.select_by_value(gender)

elem = driver.find_element_by_name("handphone")
elem.clear()
elem.send_keys(handphone)

# Find element based on name, then click the element
elem = driver.find_element_by_name("tou")
elem.click()
elem.send_keys(u'\ue007')

driver.close()
