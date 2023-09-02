################################################################################################
#
# Program Name  :   backend_testing.py
#
# Creation Date :   19-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is a testing program for REST API and database functions.
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
################################################################################################
import requests

res = requests.post('http://127.0.0.1:5000/data/15', json={"user_name":"Matthew"})
if res.ok:
    print("Successful to add new user")

    res2 = requests.get('http://127.0.0.1:5000/data/15', json={"user_id":"15"})

    print(res2.json())
else:
    print("Failed to add new user")