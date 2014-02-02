import MySQLdb

db = MySQLdb.connect(host='localhost',
                     user='doug',
                     passwd='doug',
                     db='stackexchange')
db.set_character_set('utf8')
dbc = db.cursor()
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')
