import sqlalchemy
import pandas as pd
import numpy as np
import psycopg2
import urllib.parse as urlparse
import os
os.environ['DATABASE_URL'] = 'postgres://lpzqiiuvnsltmv:5cb622f61b28fff5acc5345387355c923babd9d846afbd02e6bacc54ec32b694@ec2-107-22-211-182.compute-1.amazonaws.com:5432/did369bmda40b'
url = urlparse.urlparse(os.environ['DATABASE_URL'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port

con = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
            )

#def __init__(self):
#    pass

"""def connect( user, password, db, host='localhost', port=5432):
    '''Returns a connection and a metadata object'''
    # We connect with the help of the PostgreSQL URL
    # postgresql://federer:grandestslam@localhost:5432/tennis
    url = 'postgresql://{}:{}@{}:{}/{}'
    url = url.format(user, password, host, port, db)

    # The return value of create_engine() is our connection object
    con = sqlalchemy.create_engine(url, client_encoding='utf8')

    # We then bind the connection to MetaData()
    meta = sqlalchemy.MetaData(bind=con, reflect=True)

    return con, meta

con, meta = connect('postgres','pokemon1995','tradingbot') 

from sqlalchemy import Table, Column, Integer, String, Float

db = Table('tick', meta,
    Column('date', Float, primary_key=True),
    Column('price', Float),
    Column('trend', Float),
    Column('SMA', Float),
    Column('RSI', Float),
    Column('short', Float),
    Column('long', Float),
    Column('closedLong', Float),
    Column('closedShort', Float)
)
db = meta.tables['tick']

with con.connect() as conn:
    # Create the above tables
    #   db.create()
    #insert_statement = db.insert().values(date='2001-02-16 20:00:00',price=3.21,trend=2.33,sma=5.43,rsi=30.42,short=26.53,long=30.44)
    #insert_statement = db.insert().values(date='2001-02-16 20:00:00',closedlong=354,typeoftrade="short")
    #conn.execute(insert_statement)
    # Update
    #update_statement = db.update().where(db.c.date=='2001-02-16 20:00:00').values(closedlong=354,typeoftrade="short")
    #conn.execute(update_statement)
    # Read
    #select_statement = db.select()
    #result_set = conn.execute(select_statement)
    #for r in result_set:
    #  print(r)
    #READ
    #result_set = conn.execute("SELECT date FROM tick")
    #print (result_set)
    #delete
    #conn.execute("DELETE FROM tick WHERE date ='2001-02-16 20:00:00'")

    #OR
    # Delete
    #delete_statement = film_table.delete().where(film_table.c.year == "2016")
    #conn.execute(delete_statement)


    df = pd.read_sql_table('tick', con)
tradeplacedlist = df['cryptoamount'].tolist()
print ((tradeplacedlist))
tradeplacedlist = [i for i in tradeplacedlist if i*0  == 0]
print ((tradeplacedlist))
##pricelist = df['price'].tolist()
#print (datelist)"""
