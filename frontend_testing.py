##############################################################################################
#
# Program Name  :   frontend_testing.py
#
# Creation Date :   19-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is a testing program for the Web interface
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
###############################################################################################
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

str =""

driver = webdriver.Chrome(service=Service())
driver.get("http://127.0.0.1:5001/users/get_user_data/2")
print("Current URL :" + driver.current_url)
print("Page Source :" + driver.page_source)

try:
#    driver.find_element(By.XPATH, value="//input[@type='user_name']")
#    print(driver.find_element(By.XPATH, value="//input[@type='user']"))
    print(driver.find_element(By.XPATH, value="//tagname[@attribute='user']"))
except:
    print("Unable to locate element")

time.sleep(5)
driver.quit()




