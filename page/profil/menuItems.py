from kivymd.uix.card import MDCard

from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.screenmanager import ScreenManager
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle

from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDIconButton
from kivy.uix.scrollview import ScrollView
from kivymd.uix.button import MDTextButton
from kivymd.uix.list import OneLineIconListItem, MDList, IconLeftWidget

from kivy.graphics import Color, RoundedRectangle
from database.session import session

from components.popup import CustomPopup

# nantik gunakan ini ke tombol logout untuk menghapus chace dari session agar bisa di arahkan ke halaman login
# session.drop_data_sesio


class widgetMenuItem(BoxLayout):
    """menu menu di bawah"""

    # items: list[str] = ["settings", "daftar file", "logout"]
    items = {
        "settings": "cog",
        "daftar file": "folder",  # folder cocok utk daftar file
        "logout": "logout",
    }

    def __init__(self, screen_manager: ScreenManager):
        super().__init__()
        self.orientation = "vertical"
        self.padding = 10
        self.spacing = 15

        self.screen_manager = screen_manager

        self.mainLayout: MDBoxLayout = MDBoxLayout(
            orientation="horizontal", padding=10, spacing=10
        )

        with self.canvas.before:
            Color(0.75, 0.75, 0.75, 1)
            bgMain = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(
            pos=lambda instace, value: self._update_bg_pos(bgMain, value),
            size=lambda instace, value: self._update_bg_size(bgMain, value),
        )

        # card yg horizintal
        self.mainLayout.add_widget(self.widgetSectionRight())
        self.mainLayout.add_widget(self.widgetsectionRight())

        # ketika windows berubah
        Window.bind(on_resize=self.upgrade_windows)
        # main layout utama
        self.add_widget(self.mainLayout)

    def widgetSectionRight(self) -> ScrollView:
        """section"""
        scroll: ScrollView = ScrollView()
        # warna scroll , langsong di canvas agar tidak ada terlalu banyak wrapper class baru
        with scroll.canvas.before:
            Color(0.0, 0.639, 1.0, 1)
            bgSectionnRight = RoundedRectangle(size=scroll.size, pos=scroll.pos)
        scroll.bind(
            size=lambda instace, v: self._update_bg_size(bgSectionnRight, v),
            pos=lambda instace, v: self._update_bg_pos(bgSectionnRight, v),
        )

        listview = MDList()
        for text, icon_name in self.items.items():
            item = OneLineIconListItem(
                text=text,
                # bg_color=[0.0, 0.639, 1.0, 1],
                on_release=lambda x, i=text: self._on_release_btn_trigger(x, i),
            )
            item.add_widget(
                IconLeftWidget(
                    icon=icon_name,
                    theme_text_color="Custom",
                    text_color=[0.9, 0.9, 0.9, 1],
                )
            )
            listview.add_widget(item)

        scroll.add_widget(listview)

        return scroll

    def widgetSectionLeft(self) -> MDCard:
        """bagian atau menu di sebelah kiri"""
        layout = MDCard(
            orientation="vertical", md_bg_color=[0.4, 0.8, 0.4, 1], padding=10
        )
        layout.add_widget(MDLabel(text="profile"))
        return layout

    def _on_release_btn_trigger(self, instace, item: str):
        # screen_item = re.sub(r'[-_+=,\.]+', "", item)
        screen_item = item.replace(" ", "-")
        if item != "logout":  # jika bukan logout
            self.screen_manager.current = screen_item
            return
        else:
            popupLogout = CustomPopup(
                posisi_popup=(100, 100), title="Logout", size_popup=(200, 300)
            )
            popupLogout.set_content(self.widgetLogout())
            popupLogout.show()

    def widgetLogout(self) -> MDCard:
        card = MDCard(
            padding=10,
            spacing=10,
            md_bg_color=[0.75, 0.15, 0.13, 1],
        )
        btnlogout = MDIconButton(
            icon="trash",
            padding=8,
            on_release=lambda instance, x: session.drop_data_sesion(),
        )

        card.add_widget(MDLabel(text="Are you sure to logout"))
        card.add_widget(btnlogout)
        return card

    def _update_bg_pos(self, instance, pos):
        """Update pos bacground"""
        instance.pos = pos

    def _update_bg_size(self, instance, size):
        """update size untu bacground"""
        instance.size = size

    def upgrade_windows(self, windows, width, height):
        """update jika ada perubahan windows"""
        # Pilih breakpoint — sesuaikan kalau mau lebih sensitif
        should_vertical = (width <= 700) or (width < height)

        # jangan set ulang jika sama
        new_orient = "vertical" if should_vertical else "horizontal"
        if self.mainLayout.orientation == new_orient:
            return
        # ubah orientasi
        self.mainLayout.orientation = new_orient
