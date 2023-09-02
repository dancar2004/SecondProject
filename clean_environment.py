################################################################################################
#
# Program Name  :   clean_environment.py
#
# Creation Date :   1-Sep-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This program will stop the WEB and REST app at your environment
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
################################################################################################
import requests

#
# Stop the REST App Server at port 5000
#
try:
    res = requests.get('http://127.0.0.1:5000/stop_server')
    if res.ok:
        print("Successful to stop the REST App Server")
except Exception as err:
    print("Failed to stop the REST App Server : {err}")


#
# Stop the WEB Server at port 5001
#
try:
    res2 = requests.get('http://127.0.0.1:5001/stop_server')
    if res2.ok:
        print("Successful to stop the WEB Server")
except Exception as err:
    print("Failed to stop the WEB Server : {err}")