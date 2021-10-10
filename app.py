import os
import requests, json

import mysql.connector
from jsql import sql
from pprint import pprint
from sqlalchemy import create_engine

DATABASE_NAME = "Alsaqifa" #os.getenv("DATABASE_NAME")
DATABASE_PASSWORD = "00000000" #os.getenv("DATABASE_PASSWORD")
DATABASE_USER = "root" #os.getenv("DATABASE_USER")
DATABASE_HOST = "127.0.0.1" #os.getenv("DATABASE_HOST")

engine = create_engine(f'mysql+mysqlconnector://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}')

def database_query():

    conn = engine.connect() #start connection to database
    transaction = conn.begin() # begin transaction

    #sql is from jsql which is a tool developed by CTO of noon, to handle alot of sql related security checks, like sql injection and more.
    # it takes connection object, sql query, and paramaters if any.
    # it is followed by one of these:
    # .scalar() to return a single value.
    # .dict() to return a single row.
    # .dicts() to return a list of rows.
    # .lastrowid returns the last row id that was created.
    # and more but I didn't need them yet.
    
    user_id = sql(conn,
        '''
            SELECT 
                user_id
            FROM 
                session_tokens 
            WHERE token = :token
        '''
        ,token="hello").scalar()

    print(user_id)

    # if you want to insert a paramater just use ":" followed by the paramater name you specified in the paramaters section.
    # WHERE token = :token  <-- here
    # here --> ,token="hello").scalar()

    if everything == "good":
        transaction.commit()
    else:
        transaction.rollback()
    
    conn.close()

    return


def api_request():

        url = "https://codeforces.com/api/user.status"
        params = {
            "handle":"zakii",
            "from":1,
            "count":1
        }
        
        response = requests.get(url,params=params)
        if response.status_code == 200:
            pprint(response.json()) # pprint prints a dict in termainal in a readable way.
        else:
            print(response.errors)
 


if __name__ == '__main__':
    # database_query()
    api_request()