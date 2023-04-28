import sqlite3
con = sqlite3.connect('database.sqlite')
#con =sqlite3.connect('database.sqlite', timeout=5.0, detect_types=0, isolation_level='DEFERRED', check_same_thread=True, factory=sqlite3.Connection, cached_statements=128, uri=False)
print(type(con))
cursor =con.cursor()

""" """
query1='''CREATE TABLE user (id INTEGER PRIMARY KEY,name VARCHAR(150),email VARCHAR(150),score VARCHAR(150));'''
cursor.execute(query1)
con.commit()
con.close()
















