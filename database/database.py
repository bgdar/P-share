from tinydb import TinyDB, Query
from typing import Dict
import logging
import datetime

from components.assetsManagement import get_resource_path

from .session import session
# structure data
# {
# name : name ,
# password :password,
# create_at : 2025-12-1,
# pathfile: {
#     ....,...,..
# }
# }
#


class Db:

    def __init__(self):

        self.databasePath = get_resource_path("database", "database.json")

        self.__database = None
        self.__query = Query()

        # self.session: Session = None

    def start(self, pathDatabse):
        '''mulai database '''

        self.__database = TinyDB(pathDatabse)

    def insert_login(self, data):
        '''@param data : masukan data bertipe dictionary seperti contoh di bawah
           @example    : {name:"nama_nya",password:"password_nya"} '''
        print("data yang di dapat :", data)
        # validasi jika user sudah ada atau belum
        # if self.__database.search(self.__query.name == data['name']):
        #     logging.log(logging.INFO, f"name atas nama {
        #                 data['name']} sudah ada")
        # else:
        self.__database.insert({
            'name': data['name'],
            "password": data['password'],
            "create_at": str(datetime.date.today()),
        })

    def update_pathfile(self, pathfile: str, user: str):
        '''@param pathfile : path file yang akan di simpan di database
           @param user     : user yang akan di tambah path nya gunakan dari `self.userLogin`'''
        self.database.update({'pathfile': pathfile}, self.__query.name == user)

    def cek_user_password(self, password: str, name: str) -> bool:
        if self.__database.search((self.__query.name == name) & (self.__query.password == password)):
            return True
        else:
            False

    def save(self):
        '''tutup database'''
        self.__database.close()

    def remove_pathfile(self):
        pass

    def logout(self):
        self.session.drop_data_sesion()


database = Db()
