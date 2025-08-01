from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Ellipse, RoundedRectangle, Color

from kivy.properties import StringProperty

from kivy.uix.label import Label
from kivymd.uix.button import MDRaisedButton
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.uix.widget import Widget

from kivy.clock import Clock

from components.Globalstate import Store
from components.assetsManagement import get_all_files, get_resource_path
from typing import Callable, Tuple


class HeaderSection(BoxLayout):
    # observable property  : ynag bisa di bind ke UI
    lenSelectPathFile = StringProperty()

    def __init__(self):
        super().__init__()
        self.padding = 10
        self.orientation = "vertical"
        self.windowWidth, self.windowHeight = Window.size
        # property
        # self.pathFile: list(str) = []
        # Inisialisasi value dari StringProperty
        self.lenSelectPathFile = str(len(Store.pathFileNames))

        self.add_widget(self.__headerContent())

        divItemsFiles = BoxLayout(orientation='horizontal', padding=10)
        # divItemsFiles.add_widget(self.__btn_icon(
        #     icon="file.png", event=self._toggle_show_files))

        divItemsFiles.add_widget(self.__filesContent())
        # bind untuk menampilkan data terbaru dari div container
        Store.bind(isRealoadFile=self._reaload_divGridContainer)

        self.add_widget(divItemsFiles)

        # manipulasi windows
        self.update_window(windowSize=Window.size)
        Window.bind(size=self.on_window_resize)

    def __headerContent(self) -> BoxLayout:
        divHeader = BoxLayout(orientation='horizontal', height=15)
        with divHeader.canvas.before:
            Color(0.1, 0.82, 0.5, 0.5)
            divHeaderBg = RoundedRectangle(
                radius=[10], pos=divHeader.pos, size=divHeader.size)

        # update jika ada perubahan bacground
        divHeader.bind(size=lambda instance, value: self.update_bg_size(divHeaderBg, value),
                       pos=lambda instance, value: self.update_bg_pos(divHeaderBg, value))

        divHeader.add_widget(Label(text="Your choise"))
        # ambil path file name , reload jika ada perubahan pada fileny
        # Buat label untuk jumlah file
        # Label yang akan berubah
        labelPathFile = Label()
        labelPathFile.bind(size=labelPathFile.setter('text_size'))
        labelPathFile.text = self.lenSelectPathFile
        # Bind property ke Label.text
        self.bind(lenSelectPathFile=lambda inst,
                  val: setattr(labelPathFile, 'text', val))

        divHeader.add_widget(labelPathFile)

        return divHeader

    def __filesContent(self) -> ScrollView:
        ''' menampung semua file file  ynag akan di gunakan untuk di kirim user'''
        scroll = ScrollView(bar_color=[0.23, 0.4, 0.5, 0.5], do_scroll_y=True)

        self.divGridContainer = GridLayout(spacing=5, size_hint_y=None)
        self.divGridContainer.bind(
            minimum_height=self.divGridContainer.setter('height'))

        # isi setiap file nya di sini
        # baca file yang ada di folder assert/file
        files = get_all_files()
        for file in files:  # ini sialisasi awal dan berubah nantik ketika _toggle_show_files berubah
            self.divGridContainer.add_widget(
                self.__btn_file(file['nameFile'], file['pathFile']))

        # Tampilkan container jika ada file, sembunyikan jika tidak ada
        if files:
            self.divGridContainer.opacity = 1
            self.divGridContainer.disabled = False
        else:
            self.divGridContainer.opacity = 0
            self.divGridContainer.disabled = True
        scroll.add_widget(self.divGridContainer)

        return scroll
    #
    # def _toggle_show_files(self, instance):
    #     '''toggle untuk divGridContainer'''
    #     if self.divGridContainer.opacity == 0:
    #         self.divGridContainer.opacity = 1
    #         self.divGridContainer.disabled = False
    #     else:
    #         self.divGridContainer.opacity = 0
    #         self.divGridContainer.disabled = True
    #

    def _reaload_divGridContainer(self, instance=None, value=None):
        self.divGridContainer.clear_widgets()  # hapus isinya
        # tambhakan ulang
        for file in get_all_files():
            self.divGridContainer.add_widget(
                self.__btn_file(file['nameFile'], file['pathFile']))
        # setelah semua di realod atur kembali ke False
        Store.toogle_realoadFile(False)
        # Tampilkan kembali container setelah reload
        self.divGridContainer.opacity = 1
        self.divGridContainer.disabled = False

    def __btn_file(self, filename: str, pathFile: str) -> BoxLayout:

        btn = MDRaisedButton(text=filename)
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
            # perbaharui
            self.lenSelectPathFile = str(len(Store.pathFileNames))
        else:
            divbutton.remove_widget(divStatusClick)
            Store.removePathFileName(pathFile)
            # perbaharui
            self.lenSelectPathFile = str(len(Store.pathFileNames))

    # def _update_canvas(instance, pos, size, chil, perent):
    #     '''gunakn untuk setiap winget untuk menyamakan posisi dan ukuran dengan perent'''
    #     instance.pos = pos
    #     if size:
    #         instance.size = size

    def bind_len_to_label(self, label):
        '''Hubungkan StringProperty ke Label.text'''
        def update_label(instance, value):
            label.text = value
        self.lenSelectPathFile = str(len(Store.pathFileNames))
        # Tidak bisa langsung bind, workaround:
        self.lenSelectPathFile.bind = update_label
        Clock.schedule_once(lambda dt: update_label(
            self, self.lenSelectPathFile))

    def on_window_resize(self, instance, windowSize):
        self.update_window(windowSize)

    def update_bg_size(self, rect: Widget, size: Widget.size):
        '''Gunakan utnuk mengupdate bacground size element'''
        rect.size = size

    def update_bg_pos(self, rect: Widget, pos: Widget.pos):
        '''Gunakan utnuk mengupdate bacground untuk pos element'''
        rect.pos = pos

    def update_window(self, windowSize: Tuple[int, int]):
        '''isi setiap perubahan windwos nya '''
        width, height = windowSize

        # update untuk grid
        self.divGridContainer.cols = 3 if width >= 600 or height >= 800 else 1
