from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle


class ProfilHeader(BoxLayout):
    def __init__(self):
        super().__init__()
        self.orientation = "vertical"
        with self.canvas.before:
            Color(27/255, 30/255, 35/255, 1)
            bg = Rectangle(size=self.size, pos=self.pos)

        self.bind(pos=lambda instace, value: self.update_pos(bg, value))
        self.bind(size=lambda instace, value: self.update_size(bg, value))

        self.add_widget(self.fotoProfilCard())

    def fotoProfilCard(self):
        ''' ini lingkaranya yg menampung foto profil'''
        self.divFotoProfilCard = BoxLayout(orientation='horizontal')
        self.divFotoProfilCard.add_widget(Label(text="header profile"))

        with self.divFotoProfilCard.canvas.before:
            # profileImage = Image(source=image)
            Color(0.5, 0.5, 0.5, 1)
            self.ellipse = Ellipse(size=(50, 50))

        # saya ingin utnuk bacgorun ini absolute
        # self.divFotoProfilCard.bind(size=lambda instace, vlu: self.update_size(
            # self.ellipse, vlu), pos=lambda instace, vlu: self.update_pos(self.ellipse, vlu))

        self.divFotoProfilCard.bind(
            pos=self.update_bgCicler, size=self.update_bgCicler)
        return self.divFotoProfilCard

    def update_bgCicler(self, *args):
        self.ellipse.pos = self.divFotoProfilCard.pos
        self.ellipse.size = self.divFotoProfilCard.size

    def update_size(self, rect, size):
        '''gunakan bind untuk mengupdate size
        param :
            rect : kemana akan di update (mislanya Rectangle)
            size    : size dari yang mengikuti perentenya'''
        rect.size = size

    def update_pos(self, rect, pos):
        '''gunakan bind untuk mengupdate pos
        param :
            rect : kemana akan di update (misalnay Rectangle)
            size    : pos dari yang mengikuti perentenya'''
        rect.pos = pos
