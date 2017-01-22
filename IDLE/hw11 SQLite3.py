import sqlite3

conn= sqlite3.connect('tuturial.db')
c=conn.cursor()
def create_table():
    c.execute('create table if not exists stuffToplot(unix real,datestamp text,value real,k real)')
def data_entry():
    c.execute("insert into stuffToPlot values(145,'2016-01-01','python')")
    conn.commit()
    c.close()
    conn.close()
def select():
    f=c.execute('select * from stuffToPlot')
    print(f)
    conn.commit()
    c.close()
    conn.close()
