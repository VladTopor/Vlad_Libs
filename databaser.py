import requests
import algoritms
ip = algoritms.const("http://127.0.0.1:5000")
class DatabaseError(BaseException):
    def __init__(self,text):
        pass
class DataBase:
    def __init__(self,dbname):
        self.dbname = dbname
    def createDb(self,db_name):
        answer = requests.get(str(ip)+f"/api/db/create_db/{self.dbname}/{db_name}")
        if "Done" in answer.text:
            return True
        else:
            raise DatabaseError(f"Failed to create database {db_name}")
    def createTable(self,table_name,dbname="default"):
        answer = requests.get(str(ip)+f"/api/db/create_table/{self.dbname}/{dbname}/{table_name}")
        print(answer.text)
        if "Done" in answer.text:
            return True
        else:
            raise DatabaseError(f"Failed to create table {table_name}")
    def setContent(self,key,value,table_name="default",dbname="default"):
        answer = requests.get(str(ip) + f"/api/db/{self.dbname}/{dbname}/{table_name}/{key}/{value}")
        if "Done" in answer.text:
            return True
        else:
            raise DatabaseError(f"Failed to set value!")
    def getContent(self,key,table_name="default",dbname="default"):
        answer = requests.get(str(ip) + f"/api/db/{self.dbname}/{dbname}/{table_name}/{key}")
        if not "Fail" in answer.text:
            return answer.text
        else:
            raise DatabaseError(f"Failed to get value!")