from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout


class CustomPopup:
    """
    CustomPopup memungkinkan membuat popup dengan ukuran dan posisi tertentu.
    :param posisi_popup: Tuple (x, y) untuk posisi popup
    :param title: Judul popup
    :param size_popup: Tuple (lebar, tinggi) untuk ukuran popup
    """

    def __init__(self, posisi_popup, title, size_popup):
        self.posisi_popup = posisi_popup
        self.size_popup = size_popup
        self.title = title
        self.content_factory = None
        self.button_close = None
        self.popup = None

    def set_content(self, content_factory):
        """Atur factory function untuk konten popup
        Args:
            content_factory: Function yang mengembalikan widget baru setiap dipanggil
        """
        self.content_factory = content_factory

    def show(self):
        """Tampilkan popup ke layar"""
        if self.content_factory is None:
            raise ValueError(
                "Konten popup belum diatur. Gunakan set_content() terlebih dahulu.")

        # container baru untuk app ini
        popup_container = BoxLayout(orientation='vertical')

        # Buat konten baru setiap kali popup ditampilkan
        content = self.content_factory()
        popup_container.add_widget(content)

        # Tambahkan tombol close
        button_close = Button(text="close", size_hint_y=None, height=40)
        popup_container.add_widget(button_close)

        # lakukan akuras berdasarkan windows ukuranya
        lebarPopup, tinggiPopup = self.size_popup

        self.popup = Popup(
            title=self.title,
            content=popup_container,
            size_hint=(None, None),
            size=(lebarPopup, tinggiPopup),
            auto_dismiss=False
        )
        self.popup.pos = self.posisi_popup

        button_close.bind(on_press=self.popup.dismiss)
        self.popup.open()
