from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button


class MyApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')

        btn = Button(text='Tampilkan Popup')
        btn.bind(on_press=self.show_popup)

        root.add_widget(btn)
        return root

    def show_popup(self, instance):
        # Isi konten popup
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text='Ini popup di atas semua!'))
        close_btn = Button(text='Tutup')
        content.add_widget(close_btn)

        # Buat Popup
        popup = Popup(
            title='Pesan Penting',
            content=content,
            size_hint=(0.7, 0.3),  # lebar 70% layar, tinggi 30%
            auto_dismiss=False    # agar hanya bisa ditutup lewat tombol
        )

        close_btn.bind(on_press=popup.dismiss)
        popup.open()


MyApp().run()
