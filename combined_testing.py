##########################################################################################################
#
# Program Name  :   combined_testing.py
#
# Creation Date :   19-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is a combined testing program for WEB interface, REST API and database functions.
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
############################################################################################################
import time
import requests
import pymysql
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

request_data = []
user_name = ""
user_id = 30
schema_name = "mydb"

####################################################################
# Part 1 : Post any new user data to the REST API using POST method.
####################################################################
res = requests.post('http://127.0.0.1:5000/data/30', json={"user_name":"Samuel"})
if res.ok:
    print("Successful to add new user")
else:
    print("Failed to add new user")

#############################################################################
# Part 2 : Submit a GET request to make sure data equals to the posted data.
#############################################################################
res2 = requests.get('http://127.0.0.1:5000/data/30', json={"user_id":"30"})
if res2.ok:
    print("Successful to query the user")
    print(res2.json())
else:
    print("Failed to query the user")

################################################################################
# Part 3 : Using pymysql, check posted data was stored inside DB (users table).
################################################################################
# Establishing a connection to DB
conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
conn.autocommit(True)
cursor = conn.cursor()

try:
    cursor.execute(f"SELECT * FROM {schema_name}.users WHERE ID = '{user_id}';")
except pymysql.Error as err_msg:
    print("Error to query user with error pymysql %d: %s" %(err_msg.args[0], err_msg.args[1]))
finally:
    print("Finally of query user")

for row in cursor:
    print("Use pymysql to check the posted data")
    print(row)
    request_data.append(row)

cursor.close()
conn.close()

##############################################
# Part 4 : Start a Selenium Webdriver session.
##############################################
driver = webdriver.Chrome(service=Service())

################################################################
# Part 5 : Navigate to web interface URL using the new user id.
################################################################
driver.get("http://127.0.0.1:5001/users/get_user_data/30")
print("Current URL :" + driver.current_url)
print("Page Source :" + driver.page_source)

###############################################
# Part 6 : Check that the user name is correct
###############################################
try:
    driver.find_element(By.XPATH, value="//input[@type='user_name']")
except:
    print("Unable to locate element")

time.sleep(5)
driver.quit()

