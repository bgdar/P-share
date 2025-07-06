import os

from kivy.uix.filechooser import FileChooserListView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from kivy.utils import platform

from plyer import filechooser

from components.popup import CustomPopup
from components.infoPopup import InfoPopup

from network import get_ip_address
import shutil

current_dir = os.path.dirname(__file__)
folder_file = os.path.join(current_dir, "../../assets/file/")
os.makedirs(folder_file, exist_ok=True)  # buat dulu jika belum ada


def file_selected_PC(instance, selection, touch=None):
    if selection:
        for file in selection:
            try:
                shutil.copy(file, folder_file)
                notif = InfoPopup(f'file {file} di salin', 'succes', 3)
                notif.Show_popup()

            except Exception as e:
                print("Gagal menyalin:", file)
                print("Error:", e)

            print("file di pilih ", file)


def file_selected_Mobile(selection: list):
    if selection:
        print(f"File dipilih:\n{selection[0]}")
        # salin file yg di pilih ke dir '/assets/file'
        shutil.copy(selection[0], folder_file)
    else:
        print("Tidak ada file yang dipilih")


def change_path(instance, file_pc_choose: FileChooserListView):
    if os.path.isdir(instance.text):
        file_pc_choose.path = instance.text
        print("text di enter")
    else:
        # untuk sekarang gini aja dulu nantik akan di buat popup_Global
        print("path tidak valid")

# CREATE MENU


def create_upload_file():
    content = BoxLayout(orientation="vertical")

    print("platform", platform)
    if platform in ['android', 'ios']:
        filechooser.open_file(on_selection=file_selected_Mobile)
        content.add_widget(Label(text="choose file upload"))
    else:
        # managemnets file upload | semua file boleh di upload
        file_pc_choose = FileChooserListView(
            filters=["*.*"], multiselect=False)

        # pembungkus file path start
        divFilePath = BoxLayout(orientation="horizontal",
                                size_hint_y=None, height=50)
        btnEnterPath = Button(text="add", width=40, size_hint_x=None)

        textFilePath = TextInput(hint_text="path")
        textFilePath.bind(on_text_validate=lambda instance: change_path(
            instance, file_pc_choose))
        btnEnterPath.bind(on_press=lambda instance: change_path(
            textFilePath, file_pc_choose))

        file_pc_choose.bind(on_selection=file_selected_PC)  # double efentc
        file_pc_choose.bind(on_submit=file_selected_PC)

        divFilePath.add_widget(textFilePath)
        divFilePath.add_widget(btnEnterPath)
        # pembungkus path and

        content.add_widget(divFilePath)
        content.add_widget(file_pc_choose)
    return content


def create_check_ip_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text=get_ip_address()))
    return content


def create_menu3_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text="Menu 3 content"))
    return content


def create_menu4_content():
    content = BoxLayout(orientation='horizontal')
    content.add_widget(Label(text="Menu 4 content"))
    return content


# Buat popup terpisah untuk setiap menu
menuUploadFile = CustomPopup(posisi_popup=(
    100, 100), title="Upload file", size_popup=(450, 500))
menuUploadFile.set_content(create_upload_file)

cekIpPopup = CustomPopup(posisi_popup=(
    100, 100), title="Your IP", size_popup=(200, 300))
cekIpPopup.set_content(create_check_ip_content)

menu3Popup = CustomPopup(posisi_popup=(
    100, 100), title="Menu 3", size_popup=(200, 300))
menu3Popup.set_content(create_menu3_content)

menu4Popup = CustomPopup(posisi_popup=(
    100, 100), title="Menu 4", size_popup=(200, 300))
menu4Popup.set_content(create_menu4_content)


# katagory popup
infoUploadFile = InfoPopup(
    title="Click 2 kali untuk save file", type='info', timer=3)

infoIp = InfoPopup(title="ip computer kamu", type='info', timer=2)

# menu yang akan di gunakan di Dashboard
Menu = [
    # gunakan untuk mendapakan ip yg bisa di gunakan
    {"menu": "upload", "to": "", "popup": menuUploadFile, "popupInfo": infoUploadFile},
    {"menu": "cek ip", "to": "", "popup": cekIpPopup, "popupInfo": infoIp},
    {"menu": "menu3", "to": "", "popup": menu3Popup, "popupInfo": ""},
    {"menu": "menu4", "to": "", "popup": menu4Popup, "popupInfo": ""},
]
