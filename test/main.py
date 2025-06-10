from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle


class MyWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        with self.canvas:  # arahkan ke winget
            Color(1, 0, 0, 1)  # Merah solid (r=1, g=0, b=0, a=1)
            Rectangle(pos=(100, 100), size=(200, 100))


class MyApp(App):
    def build(self):
        return MyWidget()


MyApp().run()
