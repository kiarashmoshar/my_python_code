import sqlite3
with sqlite3.connect("sample.db") as connection:
    c=connection.cursor()
    #c.execute("drop table posts")
    c.execute("create table posts(title text,describtion text)")
    c.execute('insert into posts values("good","I\'m good.")')
    c.execute('insert into posts values("well","I\'m well.")')
