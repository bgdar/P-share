from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock

from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField

from components.infoPopup import InfoPopup

from database.session import session
from database.database import database


class SignUp(Screen):
    def __init__(self, screen_manager, **kwargs):
        super().__init__(**kwargs)
        self.screenManager: ScreenManager = screen_manager

        mainLayout = BoxLayout(orientation="vertical")
        mainLayout.add_widget(MDLabel(text="Sign Up", halign="center"))

        mainLayout.add_widget(self.popupSingUp())
        self.add_widget(mainLayout)

    def popupSingUp(self) -> BoxLayout:
        divPopupSignUp = BoxLayout(orientation="vertical")

        textName = MDTextField(hint_text="masukan nama kamu ")
        textPassword = MDTextField(
            hint_text="masukan password kamu", password=True)
        textEmail = MDTextField(hint_text="email")

        divPopupSignUp.add_widget(textName)
        divPopupSignUp.add_widget(textPassword)
        divPopupSignUp.add_widget(textEmail)

        btnSubmit = MDRaisedButton(text="Submit", pos_hint={"center_x": 0.5})
        divPopupSignUp.add_widget(btnSubmit)

        btnSubmit.bind(on_release=lambda instace: self._handleButtonSubmit(
            instace, textName=textName, textPassword=textPassword, textEmail=textEmail))

        return divPopupSignUp

    def _handleButtonSubmit(self, instace, textName: MDTextField, textPassword: MDTextField, textEmail: MDTextField):
        if len(textName.text) <= 0:
            InfoPopup("warning", "isi dulu nama kamu", 1.5).show_popup()
        elif len(textPassword.text) <= 0:
            InfoPopup("masukin dulu password nya ", "warning", 1.5)
        else:
            # create session dan database

            database.insert_login(
                {"name": textName.text, "password": textPassword.text, "email": textEmail.text})

            InfoPopup("success create your accont", "succes", 1.5).show_popup()
            Clock.schedule_once(
                lambda detime: self.__redirect_page("signIn"), 1.6)

    def __redirect_page(self, pageName):
        self.screenManager.current = pageName
