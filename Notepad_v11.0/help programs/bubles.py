from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivy.metrics import dp

class CustomBubbleApp(App):
    def build(self):
        self.root = FloatLayout()

        # TextInput БЕЗ стандартного пузыря
        self.text_input = TextInput(
            text='Выделите текст и удерживайте для меню',
            size_hint=(0.8, 0.2),
            pos_hint={'center_x': 0.5, 'top': 0.7},
            use_bubble=False,  # Отключаем стандартное меню
            multiline=True
        )
        self.text_input.bind(on_touch_down=self.on_textinput_touch)
        self.root.add_widget(self.text_input)

        return self.root

    def on_textinput_touch(self, instance, touch):
        if instance.collide_point(*touch.pos):
            # Запускаем проверку на долгое нажатие (1 сек)
            Clock.schedule_once(self.show_custom_bubble, 1)

    def show_custom_bubble(self, dt):
        # Рассчитываем позицию над TextInput
        input_x = self.text_input.x
        input_y = self.text_input.y
        input_height = self.text_input.height

        bubble_y = input_y + input_height + dp(10)  # 10dp отступа сверху

        # Создаём кастомный пузырь
        self.current_bubble = Bubble(
            size_hint=(None, None),
            size=(280, 180),
            pos=(input_x, bubble_y)
        )

        # Контейнер для кнопок
        layout = BoxLayout(
            orientation='vertical',
            spacing=dp(8),
            padding=dp(12)
        )

        # Кнопки с русскими подписями
        cut_btn = BubbleButton(text='Вырезать')
        cut_btn.bind(on_press=self.cut_text)

        copy_btn = BubbleButton(text='Копировать')
        copy_btn.bind(on_press=self.copy_text)

        paste_btn = BubbleButton(text='Вставить')
        paste_btn.bind(on_press=self.paste_text)

        select_all_btn = BubbleButton(text='Выделить всё')
        select_all_btn.bind(on_press=self.select_all_text)

        layout.add_widget(cut_btn)
        layout.add_widget(copy_btn)
        layout.add_widget(paste_btn)
        layout.add_widget(select_all_btn)

        self.current_bubble.add_widget(layout)
        self.root.add_widget(self.current_bubble)

    def cut_text(self, instance):
        if self.text_input.selection_text:
            self.text_input.cut()
        self.close_bubble()

    def copy_text(self, instance):
        if self.text_input.selection_text:
            self.text_input.copy()
        self.close_bubble()

    def paste_text(self, instance):
        self.text_input.paste()
        self.close_bubble()

    def select_all_text(self, instance):
        self.text_input.select_all()
        self.close_bubble()

    def close_bubble(self):
        if self.current_bubble and self.current_bubble in self.root.children:
            self.root.remove_widget(self.current_bubble)
            self.current_bubble = None

if __name__ == '__main__':
    CustomBubbleApp().run()
