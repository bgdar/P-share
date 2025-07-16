from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Ellipse, Color
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget

from components.Globalstate import Store
from components.assetsManagement import get_all_files, get_resource_path
from typing import Callable, Tuple
from components.infoPopup import InfoPopup

import os


class HeaderSection(BoxLayout):
    def __init__(self):
        super().__init__()
        self.padding = 10
        self.orientation = "vertical"
        self.windowWidth, self.windowHeight = Window.size
        # property
        # self.pathFile: list(str) = []

        self.add_widget(self.__headerContent())

        divItemsFiles = BoxLayout(orientation='horizontal', padding=10)
        divItemsFiles.add_widget(self.__btn_icon(
            icon="file.png", event=self._toggle_show_files))

        # bind untuk menampilkan data terbaru dari div container
        Store.bind(isRealoadFile=self._reaload_divGridContainer)
        divItemsFiles.add_widget(self.__filesContent())

        self.add_widget(divItemsFiles)

        # manipulasi windows
        self.__update_window(windowSize=Window.size)
        Window.bind(size=self.on_window_resize)

    def __headerContent(self) -> BoxLayout:
        divHeader = BoxLayout(orientation='horizontal', height=45)

        divHeader.add_widget(Label(text="Your choise"))
        # ambil data dari Global state
        divHeader.add_widget(Label(text=str(len(Store.pathFileNames))))

        return divHeader

    def __filesContent(self):
        '''divGridContainer'''
        self.divGridContainer = GridLayout(spacing=5, size_hint_y=None)
        self.divGridContainer.bind(
            minimum_height=self.divGridContainer.setter('height'))

        # isi setiap file nya di sini
        # baca file yang ada di folder assert/file
        for file in get_all_files():  # ini sialisasi awal dan berubah nantik ketika _toggle_show_files berubah
            self.divGridContainer.add_widget(
                self.__btn_file(file['nameFile'], file['pathFile']))
        print("current loop di fungsi ini allfile")

        self.divGridContainer.opacity = 0
        self.divGridContainer.disabled = True

        return self.divGridContainer

    def _toggle_show_files(self, instance):
        '''toggle untuk divGridContainer'''
        if self.divGridContainer.opacity == 0:
            self.divGridContainer.opacity = 1
            self.divGridContainer.disabled = False
        else:
            self.divGridContainer.opacity = 0
            self.divGridContainer.disabled = True

    def __btn_icon(self, icon: str, event: Callable):
        # pathIcon = os.path.join(os.path.dirname(__file__), "../assets/icon/")
        # icon_path = os.path.join(pathIcon, icon)
        icon_path = get_resource_path('assets', 'icon', icon)
        btn = Button(size=(50, 50), size_hint=(
            None, None), background_normal="")
        icon = Image(source=icon_path)
        btn.add_widget(icon)

        # btn.bind(on_press=lambda x: event(x,arg))  # jika butuh arg
        btn.bind(on_press=event)  # panggil sata di tekan

        return btn

    def _reaload_divGridContainer(self, instance=None, value=None):
        print("is running ")
        self.divGridContainer.clear_widgets()  # hapus isinya
        # tambhakan ulang
        for file in get_all_files():
            self.divGridContainer.add_widget(
                self.__btn_file(file['nameFile'], file['pathFile']))
        # setelah semua di realod atur kembali ke False
        Store.toogle_realoadFile(False)

    def __btn_file(self, filename: str, pathFile: str) -> BoxLayout:

        btn = Button(text=filename)
        divbutton = BoxLayout(orientation="vertical",
                              size_hint_y=None, height=30)
        divStatusClick = Widget(size_hint=(None, None),
                                size=(25, 25))
        # gambar menu ubult untuk tand
        with divStatusClick.canvas.before:
            Color(1, 0, 0, 1)
            ellips = Ellipse(pos=divStatusClick.pos, size=(15, 15))
            # tetapkan atribut val ke ellips
        divStatusClick.bind(pos=lambda instance,
                            val: setattr(ellips, 'pos', val))
        # letakkan di bawah bind agar btn tidak tertimpa
        divbutton.add_widget(btn)
       # kondisi jika divInfoClick muncul tambahkan dan jika tidak hapus kembali
        btn.bind(on_press=lambda x: self.__trigrer_btn_file(
            x, pathFile, divbutton, divStatusClick))

        return divbutton

    def __trigrer_btn_file(self, instance, pathFile: str, divbutton: BoxLayout, divStatusClick: Widget):
        '''fungsi yang terjadi saat setiap file di tekan'''
        print("path yang di dapat :", pathFile)
        if divStatusClick not in divbutton.children:
            divbutton.add_widget(divStatusClick)
            Store.setPathFileName(pathFile)
        else:
            divbutton.remove_widget(divStatusClick)
            Store.removePathFileName(pathFile)

    # def _update_canvas(instance, pos, size, chil, perent):
    #     '''gunakn untuk setiap winget untuk menyamakan posisi dan ukuran dengan perent'''
    #     instance.pos = pos
    #     if size:
    #         instance.size = size

    def on_window_resize(self, instance, windowSize):
        self.__update_window(windowSize)

    def __update_window(self, windowSize: Tuple[int, int]):
        '''isi setiap perubahan windwos nya '''
        width, height = windowSize

        # update untuk grid
        self.divGridContainer.cols = 3 if width >= 600 or height >= 800 else 1
