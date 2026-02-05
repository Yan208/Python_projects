'''
Docstring for Notepad_v11.0.mainlay
Действия для вывода редактора файла.
'''
import os
from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import (StringProperty, ObjectProperty, NumericProperty) # pylint: disable=import-error,no-name-in-module
from kivy.core.window import Window
from kivy.utils import platform
#if platform == 'android':
#from jnius import autoclass
import file_menu as fm

self_main = ObjectProperty(None)


class MainLayout(Screen):
  '''
  Docstring for MainLayout
  Для отображения редактора файла.
  '''
  print('begin class MainLayout')
  float = ObjectProperty(None)
  text_for_label = StringProperty("Текущий файл")
  button_edit = ObjectProperty(None)
  scrlv = ObjectProperty(None)
  text_area = ObjectProperty(None)
  button_menu = ObjectProperty(None)
  label_app = ObjectProperty(None)
  keyb_height = NumericProperty(0)
  
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    print("MainLayout init")
    global file_list_building, self_main # subdir,
    self_main = globals()
    self_main = self
    self.app = App.get_running_app()
    self.file_name = ''
    self.call = 0
    self.send_self_main()

  def send_self_main(self):
      fm.FileMenu.receive_self_main_in_file_menu(self, self_main=self)
  
  
  # в версии 9.0 работает 100%
  # правильно работает только 1 раз
  # def get_android_vkeyboard_height(self):
  #   if platform=='android':
  #     mActivity = autoclass('org.kivy.android.PythonActivity').mActivity
  #     Rect = autoclass('android.graphics.Rect')
  #     root_window = mActivity.getWindow()
  #     view = root_window.getDecorView()
  #     r = Rect()
  #     view.getWindowVisibleDisplayFrame(r)
  #     return Window.height-(r.bottom-r.top)

  def is_text_area(self):
    for child in self.scrlv.children:
      if child == self.text_area:
        print("text_area is in scrlv")
        return True
    return False
    
  def choice_file_mainlay(self, file_list_building):
    print("file:", file_list_building.text)
    self.text_for_label = file_list_building.text
    self.choice_file(file_list_building)
  
  def back_to_file(self):
    self.app.sm.get_screen('menu_file').back_from_ml = True
    self.text_area.focus = False
    self.save_file()
    fm.self_file.build_file_menu()
    self.app.sm.current = 'menu_file'

  def off_text_area(self):
    '''
    Docstring for off_text_area
    Отключение text_area с экрана.
    '''
    self.save_file()
    self.ids.text_area.remove_widget(self.text_area)
  

  def create_file_off(self):
    '''
    Docstring for create_file_off
    Отключение create_file с экрана    
    '''
    self.save_file()
    self.ids.text_area.remove_widget(self.text_area)

  def create_file_building(self):
    '''
    Docstring for create_file_building
    Включение виджетов create_file
    '''
    self.text_for_label = "Новая заметка"
    self.text_area.text = ""
    if platform == 'android':
      self.text_area.bind(keyboard=self.on_keyb)
      self.text_area.bind(focus=self.off_keyb)
  

  def open_in_area(self):
    '''
    Docstring for open_in_area
    прочесть текущий файл в объект text_area. вызываем из choice_file()    
    '''
    if os.path.isfile(self.file_name):
      try:
        with open(self.file_name, 'r', encoding='utf-8') as file:
          self.text_area.text = file.read()
      except UnicodeDecodeError:
        try:
          with open(self.file_name, 'r', encoding='cp1251') as file:
            self.text_area.text = file.read()
        except UnicodeDecodeError:
          self.text_area.text = "Ошибка: не удалось определить кодировку файла"

    if platform == 'android':
      self.text_area.bind(keyboard=self.on_keyb)
      self.text_area.bind(focus=self.off_keyb)

  def save_file(self):
    '''
    Docstring for save_file
    # Файловая функция
    # сохраняем из text_area в текущий файл
    # вызывается из back_to_file и on_stop при условии, что self.is_text_area = True
    '''
    print('save_file begin')
    index_of_cr = self.text_area.text.find("\n")
    if index_of_cr == -1:
      self.file_name = self.text_area.text + ".txt"
    else:
      self.file_name = self.text_area.text[0:index_of_cr] + ".txt"
    if self.file_name == ".txt":
      self.app.sm.get_screen('menu_file').text_for_label = "Не сохранил"
      return
    print("имя файла:", self.file_name)
    try:
      with open(self.file_name, 'w') as file:
        file.write(self.text_area.text)
      self.app.sm.get_screen('menu_file').text_for_label = f'Сохранил в {self.file_name}'
      print('сохранил и сменил лэйбл')
    except:
      print("ОШИБКА ЗАПИСИ")
      self.app.sm.get_screen('menu_file').text_for_label = f'ОШИБКА: {self.file_name[:90]}'
    finally:
      print("попытка сохранения окончена")
    print("save_file end")

  # Файловая функция. Выбрали файлик и открываем его в объекте self.text_area
  # вызываем из on_file_list
  def choice_file(self, file_list_building):
    print("File choice pressed.")
    self.file_name = file_list_building.text
    self.open_in_area()
    return
  
  def off_keyb(self, *args):
    print('off_keyb begin')
    if self.ids.text_area.focus == False:
      self.ids.text_area.size_hint = (0.9, 0.8)
      self.ids.text_area.pos_hint = { 'x': 0.05, 'y': 0.1 }
  
  def on_keyb(self, text_area, keyb):
    print('on_keyb begin')
    self.call += 1
    #print(f'Вызывается {self.call} раз.')
    if self.call == 1:
    #правильно работает только 1 раз, хреново работает вообще
      #self.keyb_height = self.get_android_vkeyboard_height() + 200
      self.keyb_height = 1100
      # 2х соточка, чтобы над клавой слова появлялись
      
    #print('keyb_height jnius: ', self.keyb_height)
    menu_height = 100
    y_pos_ta = 1 - (Window.height - self.keyb_height + menu_height) / Window.height
    y_size_ta = (Window.height - self.keyb_height - menu_height) / Window.height
    #устанавливаем размер и положение text_area
    self.ids.text_area.size_hint = (0.9, y_size_ta)
   # self.size = (Window.width, Window.height - keyb_height - menu_height)
    self.ids.text_area.pos_hint = { 'x': 0.05, 'y': y_pos_ta }
      