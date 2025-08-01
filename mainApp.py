import os
# from kivy.app import App
from kivymd.app import MDApp  # replace karena sekarang menggunakan kivymd

from kivy.uix.screenmanager import ScreenManager
from kivy.uix.floatlayout import FloatLayout
# page module
from page.dashboard.dashboard import DashboardScreen
from page.share.share import ShareScreen
from page.profil.profil import ProfilScreen

from components.infoPopup import InfoPopup

from database.session import session
from database.database import database

from user.signIn import SignIn
from user.signUp import SignUp

from page.profil.screenItems.settings import Settings
from page.profil.screenItems.daftarFile import DaftarFile

daftarScreen = {
    "dashboard": DashboardScreen,  # akan muncul sebagai tampilan utama
    "share": ShareScreen,
    "profil": ProfilScreen,
    # daftar screen untuk user
    "signIn": SignIn,
    "signUp": SignUp,
    # screen yang akan di gunakan di profile
    "settings": Settings,
    "daftar-file": DaftarFile,
}


class mainApp(MDApp):
    def __init__(self, **kywargs):
        super().__init__(*kywargs)

        self.screenManager = ScreenManager()
        self.root_layout = FloatLayout()  # layout utama untuk menghandle popup

        self.root_layout.add_widget(self.screenManager)

    def build(self):
        self.title = "P share"

        for name, screen_class in daftarScreen.items():
            # name adalah nama screen yg aktif ,
            #!perhatian screen_manager akan di kirim ke setiap componets
            # jadi perhaikan agar tidak masuk ke parameter **kywargs
            self.screenManager.add_widget(
                screen_class(name=name, screen_manager=self.screenManager))

        return self.root_layout
    # Saat aplikais pertama kali di jalankan

    def on_start(self):
        print("apliakasi Running")
        database.start(database.databasePath)

        # AUTH cache sesion
        # di sini saya validari Aut karena di gunakan di banyak screen nantik
        if session.get_data_session():
            self.screenManager.current = "dashboard"
        else:
            self.screenManager.current = "signIn"

    # Saat aplikasi di Tutup (tidak secara pakasa)

    def on_stop(self):
        print("palikasi di tutup")
        session.save()
        database.save()

    # gunakan untuk di pangggil nantik di setiap sub
    def show_popup(self, title: str, type: str, timer: float = 1.5):
        '''akses dengan app =
                from kivymd.app import MDApp
                MDApp.get_running_app() 
              app.show_popup("Ini dari Komponen lain!","sucess",1.4)'''
        infoPopup = InfoPopup(title=title, type=type, timer=timer)
        infoPopup.show_popup()

        # Pastikan popup berada di layer teratas dengan menambahkannya terakhir
        # Jika ada popup lama, hapus dulu untuk mencegah penumpukan
        existing_popups = [
            child for child in self.root_layout.children if isinstance(child, InfoPopup)]
        for popup in existing_popups:
            self.root_layout.remove_widget(popup)

        # Tambahkan popup baru ke layer teratas
        self.root_layout.add_widget(infoPopup)


if __name__ == "__main__":
    mainApp().run()
