import os

# from kivy.app import App
from kivymd.app import MDApp  # replace karena sekarang menggunakan kivymd

from kivy.uix.screenmanager import ScreenManager

# page module
from page.dashboard.dashboard import DashboardScreen
from page.share.share import ShareScreen
from page.profil.profil import ProfilScreen

from database.session import session
from database.database import database

from user.signIn import SignIn
from user.signUp import SignUp
daftarScreen = {
    "dashboard": DashboardScreen,  # akan muncul sebagai tampilan utama
    "share": ShareScreen,
    "profil": ProfilScreen,
}


class mainApp(MDApp):
    def __init__(self, **kywargs):
        super().__init__(*kywargs)

        self. screenManager = ScreenManager()

    def build(self):
        self.title = "P share"

        for name, screen_class in daftarScreen.items():
            # name adalah nama screen yg aktif ,
            #!perhatian screen_manager akan di kirim ke setiap componets
            # jadi perhaikan agar tidak masuk ke parameter **kywargs
            self.screenManager.add_widget(
                screen_class(name=name, screen_manager=self.screenManager))

        # daftar screean untuk user
        self.screenManager.add_widget(
            SignIn(screan_manager=self.screenManager, name="signIn"))
        self.screenManager.add_widget(
            SignUp(screen_manager=self.screenManager, name="signUp"))

        return self.screenManager
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


if __name__ == "__main__":
    mainApp().run()
