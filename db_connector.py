########################################################################################################################
#
# Program Name  :   db_connector.py
#
# Creation Date :   17-Aug-2023
#
# Created By    :   Daniel H Y KONG
#
# Description   :   This is the db to provide the SELECT/INSERT/UPDATE/DELETE functions to the target database.
#
# Amendment History : <Date> <Name> <Description>
# ---------------------------------------------
#
########################################################################################################################

import pymysql

def add_user(user_id, user_name):
    result_flag = False
    schema_name = 'mydb'

    # Establishing a connection to DB

    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Inserting data into table
    try:
        cursor.execute(f"INSERT into {schema_name}.users (name, id) VALUES ('{user_name}', '{user_id}')")
        result_flag = True
    except pymysql.Error as err_msg:
        result_flag = False
        print("Error to handle add_user() with error pymysql %d: %s" %(err_msg.args[0], err_msg.args[1]))
    finally:
        print("Finally of add_user()")

    cursor.close()
    conn.close()

    if result_flag == True:
        print('result_flag is TRUE')
    else:
        print('result_flag is FALSE')

    return result_flag

def query_user(user_id):
    result_flag = False
    request_data = []
    user_name = ""
    schema_name = "mydb"

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)
    cursor = conn.cursor()

    try:
        cursor.execute(f"SELECT NAME FROM {schema_name}.users WHERE ID = '{user_id}';")
        result_flag = True
    except pymysql.Error as err_msg:
        print("Error to handle query_user() with error pymysql %d: %s" %(err_msg.args[0], err_msg.args[1]))
    finally:
        print("Finally of query_user()")

    for row in cursor:
        print(row)
        request_data.append(row)

    cursor.close()
    conn.close()

    if result_flag == True:
        try:
            user_name = request_data[0]
        except IndexError:
            print("Null return from query_user()")
    else:
        user_name = ""

    return user_name

def modify_user(user_id, user_name):
    result_flag = False
    schema_name = 'mydb'

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Update data of table
    try:
        cursor.execute(f"UPDATE {schema_name}.users SET name = '{user_name}' where ID = '{user_id}';")
        result_flag = True
    except pymysql.Error as err_msg:
        result_flag = False
        print("Error to handle modify_user() with error pymysql %d: %s" %(err_msg.args[0], err_msg.args[1]))
    finally:
        print("Finally of modify_user()")

    cursor.close()
    conn.close()

    return result_flag

def delete_user(user_id):
    result_flag = False
    schema_name = 'mydb'

    # Establishing a connection to DB
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='user', passwd='password', db=schema_name)
    conn.autocommit(True)

    # Getting a cursor from Database
    cursor = conn.cursor()

    # Delete data of table
    try:
        cursor.execute(f"DELETE FROM {schema_name}.users WHERE ID = '{user_id}';")
        result_flag = True
    except pymysql.Error as err_msg:
        result_flag = False
        print("Error to handle delete_user() with error pymysql %d: %s" %(err_msg.args[0], err_msg.args[1]))
    finally:
        print("Finally of delete_user()")

    cursor.close()
    conn.close()

    return result_flag
