import mysql.connector
class UseDatabase():
    def __init__(self,config:dict) -> None:
        self.configuration = config

    def __enter__(self) -> 'cursor':
        self.conn = mysql.connector.connect(**self.configuration)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, exc_trace) -> None:
        self.conn.commit() 
        self.cursor.close() 
        self.conn.close()

    # def setupCon(self):
    #     self.conn = mysql.connector.connect(**self.configuration)
    #     self.cursor = self.conn.cursor()
    #     return self.cursor

    
    # def releaseCon(self) -> None:
    #     self.conn.commit() 
    #     self.cursor.close() 
    #     self.conn.close()


# class Animal():
#     def __init__(self):
#         self.nums = []

#     def incrOne(self):
#         self.nums.append(1)# = [(element + 1) for element in self.nums]

#     def __enter__(self) -> 'Animal':
#         self.nums = []
#         # self.name = 'monkey'
#         return self

#     def __exit__(self, exc_type, exc_value, exc_):
#         self.name = 'cat'
    