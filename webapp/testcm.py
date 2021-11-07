from contextManager import UseDatabase, Animal
import time

dbConfig = { 'host': '127.0.0.1', 'user': 'vsearch', 'password': 'vsearchpasswd', 'database': 'vsearchlogDb'}


# with UseDatabase(dbConfig) as cursor:
#     _SQL = """show tables;"""
#     cursor.execute(_SQL)
#     data = cursor.fetchall()


# _SQL = """select * from log"""
# db = UseDatabase(dbConfig)
# db.setupCon()
# db.cursor.execute(_SQL)
# data = db.cursor.fetchall()

# for row in data:
#     print(row)

# # db.conn.commit() 
# # db.cursor.close() 
# # db.conn.close()
# db.releaseCon()

# print(type(data))

# time.sleep(15)

# a = Animal()
# print(a.name)

with Animal() as a:
    print(a.nums)
    a.incrOne()
    a.incrOne()()
    print(a.nums)


# a = Animal()
# a.incrOne()
# a.incrOne()
# print(a.nums)



