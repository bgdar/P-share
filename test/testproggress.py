from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.progressbar import MDProgressBar
from kivy.clock import Clock


class TestApp(MDApp):
    def build(self):
        layout = MDBoxLayout(orientation="vertical", padding=20, spacing=20)

        # Progress bar
        self.progress = MDProgressBar(
            value=0,
            max=100,
            color=(1, 0.8, 0, 1),  # kuning
            radius=[10, 10, 10, 10]
        )
        layout.add_widget(self.progress)

        # Update setiap 0.1 detik
        Clock.schedule_interval(self.update_progress, 0.1)

        return layout

    def update_progress(self, dt):
        if self.progress.value < self.progress.max:
            self.progress.value += 1
        else:
            self.progress.value = 0  # ulang


TestApp().run()
