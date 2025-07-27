from tinydb import TinyDB, Query
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os
import json
import base64
from components.assetsManagement import get_resource_path


class Session:
    def __init__(self):

        pathSesiondb = get_resource_path("database", "session.json")
        print("path sesion db", pathSesiondb)
        self.user = Query()

        # Gunakan caching untuk performa
        self.sesion = TinyDB(
            pathSesiondb, storage=CachingMiddleware(JSONStorage))
        self.nameUserNow: str = ""

    # def start(self, pathdb):
    #     # Cek apakah file kosong, jika iya isi file sbg dengan default TinyDB
    #     needs_init = False
    #
    #     if not os.path.exists(pathdb) or os.stat(pathdb).st_size == 0:
    #         needs_init = True
    #     else:
    #         # Check if file contains only whitespace or invalid JSON
    #         try:
    #             with open(pathdb, 'r') as file:
    #                 content = file.read().strip()
    #                 if not content:
    #                     needs_init = True
    #                 else:
    #                     # Try to parse as JSON to validate
    #                     json.loads(content)
    #         except (json.JSONDecodeError, IOError):
    #             needs_init = True
    #
    #     if needs_init:
    #         with open(pathdb, 'w') as file:
    #             file.write('{"_default": {}}')

    def update_session(self, nameUser: str, passwordUser: str):
        '''update sesion yang menyimpan __cache__ password dan name '''
        # base64.b32encode mengembalikan byte jadi kita decodekan kembali agar bisa di simpan
        paswordEncode = base64.b32encode(passwordUser.encode()).decode()
        nameEncode = base64.b32encode(nameUser.encode()).decode()
        self.nameUserNow = nameUser

        print("running sesion data", paswordEncode, nameEncode)
        print("status sesion", self.sesion)

        self.sesion.insert({
            "name": nameEncode,
            "password": paswordEncode,
        })

    def get_data_session(self) -> bool:
        # '''Mengembalikan True jika ada session yang cocok'''
        # if not self.nameUserNow:
        #     return False
        #
        # encoded_name = base64.b32encode(self.nameUserNow.encode()).decode()
        # result = self.sesion.get(self.user.name == encoded_name)
        # return result is not None
        """
        Mengembalikan True jika ada minimal satu user valid, dan set self.nameUserNow.
        """
        # nantik periksanya 1 baris aja
        data = self.sesion.all()

        for item in data:

            # karena yg di kemablikan object maka ambil yang key "name"
            name = item.get("name")
            if name and name.strip():
                # jika data tidka ada maka isi kmbali
                # self.nameUserNow = base64.b32decode(name.encode()).decode()
                return True

            return False

    def save(self):
        '''simpan dan tutup database'''
        self.sesion.close()

    def drop_data_sesion(self):
        '''hapus semua data sesion jika tidak di perlukan'''
        self.sesion.truncate()
        self.nameUserNow = ""


session = Session()
