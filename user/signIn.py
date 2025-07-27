# kita gunkan screen terpisah yang di mna di panggil ketika belum ligi pada halaman seperti share dan profil

from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton, MDRoundFlatIconButton

from kivy.clock import Clock
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget

from components.infoPopup import InfoPopup


# database
from database.database import database
from database.session import session


class SignIn(Screen):
    def __init__(self, screan_manager: ScreenManager, **kwargs):
        super().__init__(**kwargs)

        mainLayout = BoxLayout(orientation="vertical")
        self.screanManager = screan_manager

        # popupnya di tengah
        mainLayout.add_widget(self.popupSingIn())
        # menu menu cara register misalnya buat akur baru atau nantiknya lewat google
        mainLayout.add_widget(self.infoSignIn())

        self.add_widget(mainLayout)

    def popupSingIn(self) -> BoxLayout:
        divpopupSignin = BoxLayout(orientation="vertical")

        divpopupSignin.add_widget(
            MDLabel(text="your name", halign="left", font_style="Subtitle2"))
        textName = TextInput(hint_text="nama anda")
        divpopupSignin.add_widget(textName)

        divpopupSignin.add_widget(
            MDLabel(text="your password", halign="left", font_style="Subtitle2"))
        textPassword = TextInput(
            hint_text="gunakan password yang aman", password=True)
        divpopupSignin.add_widget(textPassword)

        buttonSubmit = MDRaisedButton(text="submit", width=100, height=50)
        divpopupSignin.add_widget(buttonSubmit)
        buttonSubmit.bind(on_press=lambda instace: self._handleButtonSubmit(
            instace, textName, textPassword))

        return divpopupSignin

    def infoSignIn(self) -> BoxLayout:
        divInfoSigin = BoxLayout(orientation="horizontal")
        btnSignUp = MDRaisedButton(text="signUp", width=100, height=50)
        btnGoogle = MDRoundFlatIconButton(icon="google")
        btnFaceBook = MDRoundFlatIconButton(icon="facebook")

        divInfoSigin.add_widget(btnFaceBook)
        divInfoSigin.add_widget(btnGoogle)
        divInfoSigin.add_widget(btnSignUp)

        btnSignUp.bind(on_press=self._handleSignUp)

        return divInfoSigin

    def _handleButtonSubmit(self, instace, textName: TextInput, textPassword: TextInput):
        if len(textName.text) <= 0:
            InfoPopup("warning", "isi dulu nama kamu", 1.5).Show_popup()
        elif not database.cek_user_password(textPassword.text, textName.text):
            InfoPopup("password dan nama tidak di temukan ",
                      "warning", 1.5).Show_popup()
        elif database.cek_user_password(password=textPassword.text, name=textName.text):
            # hapus data sesion yang lama untuk di masukan baru
            session.drop_data_sesion()
            session.update_session(
                nameUser=textName.text, passwordUser=textPassword.text)

            # redirect ke dashboard
            # sesuaikan nama dengan di mainApp.pydashboard
            Clock.schedule_once(
                lambda dt: self.__redirect_page('dashboard'), 1.6)

    def _handleSignUp(self, instace):
        # pindah ke halaman SignUp
        self.screanManager.current = "signUp"

    def __redirect_page(self, pageName):
        self.screanManager.current = pageName
