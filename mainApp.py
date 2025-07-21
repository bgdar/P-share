import os

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager

# page module
from page.dashboard.dashboard import DashboardScreen
from page.share.share import ShareScreen
from page.profil.profil import ProfilScreen

iconsPath = os.path.join(os.path.dirname(
    __file__), "assets", "img", "shareMas.png")

daftarScreen = {
    "dashboard": DashboardScreen,  # akan muncul sebagai tampilan utama
    "share": ShareScreen,
    "profil": ProfilScreen,
}


class mainApp(App):
    def build(self):
        self.title = "P share"
        self.icon = iconsPath

        screenManager = ScreenManager()

        for name, screen_class in daftarScreen.items():
            # name adalah nama screen yg aktif ,
            #!perhatian screen_manager akan di kirim ke setiap componets
            # jadi perhaikan agar tidak masuk ke parameter **kywargs
            screenManager.add_widget(
                screen_class(name=name, screen_manager=screenManager))
        return screenManager


if __name__ == "__main__":
    mainApp().run()
