from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse
from kivy.uix.image import Image


class ProfilHeader(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"

        self.add_widget(self.fotoProfilCard())

    def fotoProfilCard(self):
        ''' ini lingkaranya yg menampung foto profil'''
        self.divFotoProfilCard = BoxLayout(orientation='horizontal')
        self.divFotoProfilCard.add_widget(Label(text="header profile"))

        with self.divFotoProfilCard.canvas.before:
            # profileImage = Image(source=image)
            Color(0.8, 0.8, 0.8, 1)  # Warna abu-abu terang
            self.ellipse = Ellipse(size=(50, 50))

        self.divFotoProfilCard.bind(size=lambda instace, vlu: self.update_size(
            self.ellipse, vlu), pos=lambda instace, vlu: self.update_pos(self.ellipse, vlu))

        self.divFotoProfilCard.bind(
            pos=self.update_bgCicler, size=self.update_bgCicler)
        return self.divFotoProfilCard

    def update_bgCicler(self, *args):
        self.ellipse.pos = self.divFotoProfilCard.pos
        self.ellipse.size = self.divFotoProfilCard.size

    def update_size(self, instace, size):
        '''gunakan bind untuk mengupdate size
        param :
            instace : perent
            size    : size dari yang mengikuti perentenya'''
        instace.size = size

    def update_pos(self, instace, pos):
        '''gunakan bind untuk mengupdate pos
        param :
            instace : perent
            size    : pos dari yang mengikuti perentenya'''
        instace.pos = pos
