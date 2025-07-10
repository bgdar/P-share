from kivy.uix.screenmanager import Screen
from components.navigation import ButtonNavigation
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

from kivy.core.window import Window

from network import get_all_files

import os
from typing import Callable, Tuple


# ini halaman di mana pengirim file akan mengirimkan ke server alias penerima-nya


class SerderScreen(Screen):
    def __init__(self, screen_manager: None, **kwargs):
        super().__init__(**kwargs)
        self.screen_manager = screen_manager

        mainLayout = BoxLayout(orientation="vertical")
        mainLayout.add_widget(Label(text="page serder"))

        # header di paling atas untuk menangani management file
        mainLayout.add_widget(HeaderSection())
        # menu pada bagian tengah yang menagani file di kirim
        mainLayout.add_widget(CenterSection())

        if screen_manager:
            mainLayout.add_widget(ButtonNavigation(
                screen_manager=self.screen_manager))

        self.add_widget(mainLayout)


class HeaderSection(BoxLayout):
    def __init__(self):
        super().__init__()
        self.padding = 10
        self.orientation = "vertical"
        self.windowWidth, self.windowHeight = Window.size

        self.add_widget(
            Label(text="daftar file", size_hint_y=None, height=100))

        divItemsFiles = BoxLayout(orientation='horizontal')
        divItemsFiles.add_widget(self.__btn_icon(
            icon="file.png", event=self._toggle_files))
        divItemsFiles.add_widget(self.__filesContainer())

        self.add_widget(divItemsFiles)

        # manipulasi windows
        self.__update_window(windowSize=Window.size)
        Window.bind(size=self.on_window_resize)

    def __filesContainer(self):
        '''divGridContainer'''
        self.divGridContainer = GridLayout(spacing=5, size_hint_y=None)
        self.divGridContainer.bind(
            minimum_height=self.divGridContainer.setter('height'))

        # isi setiap file nya di sini
        # baca file yang ada di folder assert/file
        # gunakan setiap file untuk di tampilkan di sini

        # validasi ukuran Grid

        for file in get_all_files():
            self.divGridContainer.add_widget(
                self.__btn_file(file['nameFile'], file['pathFile']))

        self.divGridContainer.opacity = 0
        self.divGridContainer.disabled = True

        return self.divGridContainer

    def _toggle_files(self, instance):
        '''toggle untuk divGridContainer'''
        if self.divGridContainer.opacity == 0:
            self.divGridContainer.opacity = 1
            self.divGridContainer.disabled = False
        else:
            self.divGridContainer.opacity = 0
            self.divGridContainer.disabled = True

    def __btn_icon(self, icon: str, event: Callable):
        pathIcon = os.path.join(os.path.dirname(__file__), "../assets/icon/")
        icon_path = os.path.join(pathIcon, icon)
        btn = Button(size=(50, 50), size_hint=(
            None, None), background_normal="")
        icon = Image(source=icon_path)
        btn.add_widget(icon)

        # btn.bind(on_press=lambda x: event(x,arg))  # jika butuh arg
        btn.bind(on_press=event)  # panggil sata di tekan

        return btn

    def __btn_file(self, filename: str, pathFile: str) -> Button:
        btn = Button(text=filename, size_hint_y=None, height=30)
        btn.bind(on_press=lambda x: self.send_path(x, pathFile))
        return btn

    def send_path(self, instance, pathFile: str) -> str:
        '''fungsi ini di gunakan di CenterSection untuk menerima path'''
        return pathFile

    def on_window_resize(self, instance, windowSize):
        self.__update_window(windowSize)

    def __update_window(self, windowSize: Tuple[int, int]):
        width, height = windowSize

        # update untuk grid
        self.divGridContainer.cols = 3 if width >= 600 or height >= 800 else 1


class CenterSection(BoxLayout):

    def __init__(self):
        super().__init__()
        self.orientation = 'vertical'
        self.padding = 10
        self.add_widget(self.__btn_send_file(icon="send.png"))

    def __btn_send_file(self, icon=str) -> Button:
        '''
        @param icon : file img (file.png,file.jpg..)
        '''
        pathIcon = os.path.join(os.path.dirname(__file__), "../assets/icon/")
        icon_path = os.path.join(pathIcon, icon)

        btnIcon = Image(source=icon_path)
        btn = Button(background_normal="")
        btn.add_widget(btnIcon)
        return btn
