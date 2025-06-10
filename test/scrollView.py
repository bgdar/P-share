class centerItems(GridLayout):
    def __init__(self):
        super().__init__(
            cols=2,
            size_hint_y=None,
            spacing=10,
            padding=10
        )

        self.bind(minimum_height=self.setter('height'))  # penting!

        width, height = Window.size
        self.update_layout((width, height))

        for items in menu:
            self.add_widget(self.cardItems(items["menu"], items["popup"]))

        Window.bind(size=self.on_window_resize)

    def cardItems(self, menu: str, popup: CustomPopup):
        divItems = BoxLayout(size_hint_y=None, height=100, padding=10)

        with divItems.canvas.before:
            Color(0.9, 0.9, 0.9, 1)
            bg = RoundedRectangle(
                radius=[5], pos=divItems.pos, size=divItems.size)

        def update_bg(instance, value):
            bg.pos = instance.pos
            bg.size = instance.size

        divItems.bind(pos=update_bg, size=update_bg)

        btn = Button(text=menu)
        btn.bind(on_press=lambda x: popup.show())
        divItems.add_widget(btn)
        return divItems

    def on_window_resize(self, instance, size):
        self.update_layout(size)

    def update_layout(self, size):
        width, height = size
        self.cols = 2 if width >= 600 or height >= 800 else 1
