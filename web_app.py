##################################################################################################################################
#
# Program Name  :   web_app.py
#
# Creation Date :   10-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is the web interface which will return the username of a given user id stored inside users table.
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
# 1-Sep-2023    Daniel Kong     Add method to stop the WEB service
#
#######################################################################################################################################
import pymysql
from flask import Flask, request
from db_connector import query_user

# 1-Sep-2023  start
import os
import signal
# 1-Sep-2023 end

app = Flask(__name__)

#
# This part is used for the health check of the program
#
@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_user(user_name = 'no one'):
    return 'Hello ' + user_name, 200 # status code

# accessed via <HOST>:<PORT>/users/get_user_data/<USER_ID>
@app.route('/users/get_user_data/<user_id>')
def get_user_data(user_id):
    user_name = ""

    print("Check Point of GET method")
    user_name = query_user(user_id)
    # print(user_name[0])

    if user_name == "":
        return "<H1 id='error'> no such user: " + user_id + "</H1>", 201  # status code
        # return {"status":"error","reason":"no such id"}, 500  # status code
    else:
        return "<H1 id='user'>" + user_name[0] + "</H1>", 200 # status code
        # return 'Hello ' + user_name[0], 200 # status code
        # return "<H1 id='user'>", user_name, "</H1>", 200 # status code
        # return {"status":"ok","user_name":user_name}, 200  # status code

# 1-Sep-2023  start
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
# 1-Sep-2023  end

# host is pointing at local machine address
# debug is used for more detailed logs + hot swapping
# the desired port - feel free to change
app.run(host='127.0.0.1', debug=True, port=5001)