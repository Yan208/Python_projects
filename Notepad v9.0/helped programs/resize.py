'''
Извините за недоразумение. Для того чтобы решить вашу проблему с TextInput в Kivy, вам нужно будет реагировать на изменения размеров клавиатуры и соответственно поднимать ваш интерфейс над ней. 

Вот пример кода, который позволяет реализовать данное поведение:

```python
'''
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

from kivy.clock import Clock

class MyApp(App):
  def build(self):
    self.layout = BoxLayout(
      size_hint=(None, None),
      size=(Window.width, Window.height))
    self.text_area = TextInput( 
      text= 'fuck\n'*100)
    self.layout.add_widget(self.text_area)
    self.text_area.bind(keyboard=self.on_keyb)
    self.text_area.bind(focus=self.off_keyb)
    #print(dir(MyApp))
    return self.layout
        
  def off_keyb(self, *args):
    print(Window.keyboard_height)
    if self.text_area.focus == False:
      self.text_area.size_hint = (None, None)
      self.text_area.size = (Window.width, Window.height)
      self.text_area.pos_hint = { 'x': 0, 'y': 0 }

  def on_keyb(self, *args):
    print('keyb')
    keyb_height = 900
    menu_height = 100
    y_pos_text_area = 1 - (Window.height - keyb_height - menu_height) / Window.height
    #print(y_pos_text_area)
    self.text_area.size_hint = (None, None)
    self.text_area.size = (Window.width, Window.height-keyb_height)
    self.text_area.pos_hint = { 'x': 0, 'y': y_pos_text_area }


if __name__ == '__main__':
    MyApp().run()
