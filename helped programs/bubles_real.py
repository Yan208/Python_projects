from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.clock import Clock

class ContextMenu(Popup):
    def __init__(self, text_input, pos, **kwargs):
        super().__init__(**kwargs)
        self.text_input = text_input
        self.title = ''
        self.size_hint = (None, None)
        self.size = (160, 120)
        self.pos = pos
        self.auto_dismiss = True
        self.separator_height = 0  # Убираем линию заголовка

        layout = BoxLayout(orientation='vertical', spacing=2, padding=2)

        # Кнопка «Вырезать»
        cut_btn = Button(
            text='Вырезать',
            size_hint_y=None,
            height=30,
            background_color=(0.2, 0.6, 1, 1)
        )
        cut_btn.bind(on_release=self.cut_text)
        layout.add_widget(cut_btn)

        # Кнопка «Копировать»
        copy_btn = Button(
            text='Копировать',
            size_hint_y=None,
            height=30,
            background_color=(0.2, 0.6, 1, 1)
        )
        copy_btn.bind(on_release=self.copy_text)
        layout.add_widget(copy_btn)

        # Кнопка «Вставить»
        paste_btn = Button(
            text='Вставить',
            size_hint_y=None,
            height=30,
            background_color=(0.2, 0.6, 1, 1)
        )
        paste_btn.bind(on_release=self.paste_text)
        layout.add_widget(paste_btn)

        self.add_widget(layout)

    def cut_text(self, instance):
        if self.text_input.selection_text:
            self.text_input.cut()
        self.dismiss()

    def copy_text(self, instance):
        if self.text_input.selection_text:
            self.text_input.copy()
        self.dismiss()

    def paste_text(self, instance):
        self.text_input.paste()
        self.dismiss()



class CustomTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_long_press')
        self._long_press_clock = None

    def on_touch_down(self, touch):
        if touch.is_mouse_scrolling:
            return False
        if not self.collide_point(*touch.pos):
            return False

        # Запускаем таймер для долгого нажатия
        self._long_press_clock = Clock.schedule_once(
            lambda dt: self.dispatch('on_long_press', touch), 1.0  # 1 секунда
        )
        return super().on_touch_down(touch)

    def on_touch_up(self, touch):
        if self._long_press_clock:
            self._long_press_clock.cancel()
            self._long_press_clock = None
        return super().on_touch_up(touch)

    def on_long_press(self, touch, *args):
        # Позиция меню под курсором
        menu_pos = (touch.x - 80, touch.y - 60)  # центрируем относительно касания
        menu = ContextMenu(self, pos=menu_pos)
        menu.open()


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.spacing = 10
        self.padding = 10

        # Наш кастомный TextInput с поддержкой долгого нажатия
        self.text_input = CustomTextInput(
            hint_text='Нажмите и удерживайте для меню...',
            multiline=True,
            font_size=16,
            padding=10
        )
        self.add_widget(self.text_input)



class ContextMenuApp(App):
    def build(self):
        return MainLayout()



if __name__ == '__main__':
    ContextMenuApp().run()