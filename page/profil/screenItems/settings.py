from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.list import MDList, OneLineIconListItem, IconLeftWidget


class Settings(Screen):
    def __init__(self, screen_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager
        self.colors = self.get_theme_colors()
        self.build_ui()

    def get_theme_colors(self):
        return {
            "bg_dark": [27/255, 30/255, 35/255, 1],
            "text_white": [1, 1, 1, 1],
            "abu_lembut": [0.75, 0.75, 0.75, 1],
        }

    def build_ui(self):
        layout = MDBoxLayout(orientation="vertical")
        layout.md_bg_color = self.colors["bg_dark"]

        layout.add_widget(self.build_toolbar())
        layout.add_widget(self.build_scroll_list())

        self.add_widget(layout)

    def build_toolbar(self):
        return MDTopAppBar(
            title="Settings",
            elevation=2,
            pos_hint={"top": 1},
            md_bg_color=self.colors["bg_dark"],
            specific_text_color=self.colors["text_white"],
            left_action_items=[["arrow-left", lambda x: self.on_back_press()]],
        )

    def build_scroll_list(self):
        scroll = MDScrollView()
        list_view = MDList()
        items = [
            ("account", "Account"),
            ("bell", "Notifications"),
            ("palette", "Appearance"),
            ("lock", "Privacy & Security"),
            ("headphones", "Help and Support"),
            ("information", "About")
        ]

        for icon, text in items:
            list_view.add_widget(self.create_list_item(icon, text))

        scroll.add_widget(list_view)
        return scroll

    def create_list_item(self, icon, text):
        item = OneLineIconListItem(
            text=text,
            text_color=self.colors["text_white"],
            bg_color=self.colors["bg_dark"],
            on_release=lambda x=text: self.on_item_press(x)
        )
        item.add_widget(
            IconLeftWidget(
                icon=icon,
                theme_text_color="Custom",
                text_color=self.colors["abu_lembut"]
            )
        )
        return item

    def on_back_press(self):
        """ kembali ke halaman signUp"""
        self.screen_manager.current = "profil"

    def on_item_press(self, item_text):
        print(f"Pressed on item: {item_text}")
