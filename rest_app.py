################################################################################################################
#
# Program Name  :   rest_app.py
#
# Creation Date :   17-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is the REST API gateway program which will perform the GET/POST/PUT/DELETE requests.
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
# 1-Sep-2023    Daniel Kong     Add method to stop the REST App service
#
##################################################################################################################
from flask import Flask, request
from db_connector import query_user, add_user, modify_user, delete_user

# 1-Sep-2023  start
import os
import signal
# 1-Sep-2023 end

app = Flask(__name__)

# local users storage
users = {}
# supported methods

@app.route('/hello')
@app.route('/hello/<user_name>')
def hello_user(user_name = 'no one'):
    return 'Hello ' + user_name, 200 # status code

@app.route('/data/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
def user(user_id):
    ws_name = ""
    request_data = []
    response_data = []
    ws_status = False
    # y = []
    request_data = request.json
    print(request.method)

    if request.method == 'GET':
        print("Check Point of GET method")
        ws_name = query_user(user_id)

        if ws_name == "":
            return {"status":"error","reason":"no such id"}, 500  # status code
        else:
            return {"status":"ok","user_name":ws_name}, 200  # status code
    elif request.method == 'POST':
        print("Check Point of POST method")
        # getting the json data payload from request
        # request_data = request.json
        # treating request_data as a dictionary to get a specific value from key
        ws_name = request_data.get('user_name')
        print("ws_name = " + ws_name)
        print("user_id = " + user_id)
        ws_status = add_user(user_id, ws_name)
        print("Return status of add_user() = ", ws_status)

        if ws_status == True:
            return {"status":"ok","user_added":ws_name}, 200  # status code
        else:
            return {"status":"error","reason":"id already exists"}, 500  # status code

    elif request.method == 'PUT':
        print("Check Point of PUT method")
        ws_name = request_data.get('user_name')
        # users[user_id] = ws_name
        ws_status = modify_user(user_id, ws_name)

        if ws_status == True:
            return {"status":"ok","user_updated":ws_name}, 200 # status code
        else:
            return {"status":"error","reason":"no such id"}, 500  # status code

    elif request.method == 'DELETE':
        print("Check Point of DELETE method")
        ws_status = delete_user(user_id)

        if ws_status == True:
            return {"status":"ok","user_deleted":user_id}, 200  # status code
        else:
            return {"status":"error","reason": "no such id"}, 500  # status code


# 1-Sep-2023  start
@app.route('/stop_server')
def stop_server():
    os.kill(os.getpid(), signal.CTRL_C_EVENT)
    return 'Server stopped'
# 1-Sep-2023  end

app.run(host='127.0.0.1', debug=True, port=5000)

