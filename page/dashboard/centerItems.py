from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle, RoundedRectangle

from kivy.core.window import Window

from kivymd.uix.button import MDIconButton
from kivymd.uix.label import MDLabel


# component
from components.assetsManagement import get_resource_path
from components.popup import CustomPopup
from components.infoPopup import InfoPopup


from .menuCreate import Menu


class centerItems(GridLayout):
    """menu menu item di bagin tengah"""

    def __init__(self):
        super().__init__()
        width, height = Window.size
        self.padding = 10
        self.size_hint_y = None
        self.cols = 2
        self.spacing = 10  # jarak antar i:items

        # ⬇️ Otomatis ubah tinggi layout berdasarkan jumlah widget di dalamnya
        self.bind(minimum_height=self.setter("height"))

        width, height = Window.size
        self.update_layout((width, height))

        for items in Menu:
            # panggil setiap card items
            self.add_widget(
                self.cardItems(items["menu"], items["icon"], items["popup"])
            )

        # manipulasi perubhan layout Windows nya
        self.update_layout(Window.size)
        Window.bind(size=self.on_window_resize)

    def cardItems(self, menu: str, icon: str, popup: CustomPopup) -> BoxLayout:
        """setiap card items akan mmemiliki div sendiri"""
        self.divItems = BoxLayout(
            orientation="vertical", size_hint_y=None, height=100, padding=10
        )
        # gunakan nantik
        # btn.bind(on_press=partial(self.navigate_to, to))#tambah parameter 'to'
        # divItems.add_widget(btn)
        self.divItems.add_widget(MDLabel(text=menu))
        btn = MDIconButton(
            icon=icon,
            text_color=[1, 1, 1, 1],
            md_bg_color=(27 / 255, 30 / 255, 35 / 255, 1),
            theme_text_color="Custom",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        btn.bind(on_press=lambda x: self.__onClickBtnMenu(popup))
        self.divItems.add_widget(btn)

        return self.divItems

    def __onClickBtnMenu(self, popup: CustomPopup):
        """@popupInfo: cek di file menuCreate.py dari sini di kirimnya"""
        popup.show()

    def on_window_resize(self, instance, size):
        """'fungsi yang menerima perubahan untuk di gunakan"""
        self.update_layout(size)

    def update_layout(self, size):
        """gunakan nantik untuk update layout jika ada perubahan  window"""
        width, height = size
        # untuk sekarang layout di pastikan manual
        self.cols = 2 if width >= 600 or height >= 800 else 1
