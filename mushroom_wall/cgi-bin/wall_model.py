# -*- coding: ms949 -*-

import sqlite3
from datetime import datetime

db_name = 'data/wall_db.sqlite'


def test():
    return('T_T')

def put_text(name, text):
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    result = cursor.execute("INSERT INTO wall_logs (name, content, is_text) VALUES (?,?,1)", (name, text))
    connection.commit()
    connection.close()


def put_filename(name, filename):
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    result = cursor.execute("INSERT INTO wall_logs (name, content, is_text) VALUES (?,?,0)", (name, filename))
    connection.commit()
    connection.close()




# 파라미터 문자열로 입력해야함! 06 <- 이런 것도 맞춰서 
def get_transcript_day(year, month, day):
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    day_str = year + '-' + month + '-' + day
    results = cursor.execute("SELECT name, content, datetime, is_text FROM wall_logs WHERE datetime>=Datetime('" + day_str + "') AND datetime<=Datetime('" + day_str + " 23:59:59') ORDER BY datetime")
    response = results.fetchall()
    return(response)




def get_transcript_all():
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    results = cursor.execute("SELECT name, content, datetime, is_text FROM wall_logs ORDER BY datetime")
    response = results.fetchall()
    return(response)




def get_transcript_day_list():
    connection = sqlite3.connect(db_name)
    connection.text_factory = str
    cursor = connection.cursor()
    results = cursor.execute("SELECT datetime FROM wall_logs ORDER BY datetime")
    data = results.fetchall()
    list = []
    for d in data:
        tmp = datetime.strptime(d[0], '%Y-%m-%d %H:%M:%S')
        date = tmp.date()
        if date not in list:
            list.append(date)
    
    response = []
    for d in list:
         response.append(str(d))
    
    return(response)
