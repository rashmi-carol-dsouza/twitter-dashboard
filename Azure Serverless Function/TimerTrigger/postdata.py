import pyodbc
import logging
import os

def write_to_database(df):
    server = 'enter_sever_name'
    database = 'enter_database_name'
    username = 'enter_username'
    password = 'enter_password' 
    driver = 'driver'

   
    cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()

    
    
    for index, row in df.iterrows():
        try:
            cursor.execute("INSERT INTO dbo.tweet (id,tweet_timestamp,tweet_text,sentiment,topic,tweet_time,tweet_date,tweet_day,tweet_hour) values (?,?,?,?,?,?,?,?,?)",
            row.id,row.time,row.text,row.sentiment,row.topic,row.Time,row.Date,row.Day,row.Hour)
        except Exception as e:
            logging.warn(e)
    cnxn.commit()
    cursor.close()