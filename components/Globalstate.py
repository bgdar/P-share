from kivy.event import EventDispatcher
from kivy.properties import BooleanProperty, ListProperty
import logging

# 1. gunakan saat upload file saat ada perubhan maka update fungsi files di serde.py untuk mengupdate file file nya


class GlobalState(EventDispatcher):

    isRealoadFile = BooleanProperty(False)
    # daftar isi pathFile yang di gunkan untuk mengirim file ke server nantik
    pathFileNames: list[str] = ListProperty([])

    def toogle_realoadFile(self, status: bool):
        # toggle true atau false
        # self.isRealoadFile = not self.isRealoadFile
        self.isRealoadFile = status

        logging.info("kondisi :", self.isRealoadFile)

    def setPathFileName(self, pathFileNames: str):
        logging.info("path di tamha %s", pathFileNames)
        self.pathFileNames.append(pathFileNames)

    def removePathFileName(self, pathFileNames: str):
        logging.info("di hapus : %s", pathFileNames)
        self.pathFileNames.remove(pathFileNames)

    def getPathLength(self) -> int:
        return len(self.pathFileNames)


Store = GlobalState()
