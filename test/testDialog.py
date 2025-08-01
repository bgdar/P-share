from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFlatButton

class CustomPopup(MDCard):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.size_hint = (0.3, None)
        self.height = "150dp"
        self.pos_hint = {"top": 1, "right": 1}  # 🟢 Ujung kanan atas
        self.padding = 15
        self.orientation = "vertical"
        self.md_bg_color = [1, 1, 1, 1]
        self.elevation = 8
        self.add_widget(MDLabel(text="Pesan Custom", halign="center"))
        self.add_widget(MDFlatButton(text="Tutup", on_release=self.dismiss))

    def dismiss(self, *args):
        self.parent.remove_widget(self)

class MyApp(MDApp):
    def build(self):
        self.root = FloatLayout()
        btn = MDFlatButton(text="Tampilkan", pos_hint={"center_x": 0.5, "center_y": 0.5})
        btn.bind(on_release=self.show_custom_popup)
        self.root.add_widget(btn)
        return self.root

    def show_custom_popup(self, *args):
        popup = CustomPopup()
        self.root.add_widget(popup)

MyApp().run()

