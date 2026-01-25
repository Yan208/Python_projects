from kivy.uix.screenmanager import Screen
from kivy.properties import (StringProperty, ObjectProperty)
import file_menu as fm
from kivy.uix.button import Button
import os
import popup_create_folder as pfolder
from kivy.app import App

#folder_testapp = globals()
#folder_testapp = ObjectProperty(None)
self_folder = globals()
self_folder = ObjectProperty(None)
folder_self_popupcf = globals()
folder_self_popupcf = ObjectProperty(None)

class FolderMenu(Screen):
  print('begin class FolderMenu')
  text_for_label = StringProperty("Список папок")
  grd = ObjectProperty()
  
  def __init__(self, **kwargs):
    super(FolderMenu, self).__init__(**kwargs)
    print("Folder_menu init")
    global self_main, subdir, self_folder
    self_folder = self
    self.app = App.get_running_app()
    self.grd.bind(minimum_height = self.grd.setter('height'))
    self.send_folder_menu()
    self.build_folder_menu()
    
  def send_folder_menu(self):
      pfolder.PopupCreateFolder.receive_self_folder_menu_in_popup_cr_folder(self, self_folder=self)
    
  def receive_self_popupcf_in_folder_menu(self, self_popup_create_folder):
      global folder_self_popupcf
      folder_self_popupcf = self_popup_create_folder
      
  def build_folder_menu(self):
    #global subdir
    self.on_folder_list()
    return
  
  def redraw_file(self):
    fm.self_file.build_file_menu()
    self.app.sm.current = 'menu_file'
    
  # Включение folder_list на экран
  def on_folder_list(self):
    print("on_folder_list")
    self.ids.float_folder.remove_widget(self.ids.popup_folder_box)
    self.grd.clear_widgets()
    self.subdir = self.func_folder_list()
    self.button_folder_list_menu = []
    for i in range(len(self.subdir)):
      self.button_folder_list_menu.append(i)
      self.button_folder_list_menu[i] = Button(
        text = self.subdir[i],
        background_color = (0, 0, 0, 1),
        on_release = self.choice_folder )
        #self.choice_folder_main )
      self.grd.add_widget(self.button_folder_list_menu[i])
    self.text_for_label = f"Текущая папка: {os.getcwd()}"
    return
    
  # читаем список папок в subdir
  def func_folder_list(self):
    all_list = os.listdir()
    self.folder_list = []
    self.dir_tek = os.getcwd()
    example_dir = self.dir_tek
    #'/storage/emulated/0/Documents/Pydroid3'
    with os.scandir(example_dir) as files:
      subdir = [file.name for file in files if file.is_dir()]
      subdir.insert(0, "..")
    return subdir
    
  # Файловая функция
  # Как choice_file, только для folder
  def choice_folder(self, on_folder_list):
    print("choice_folder")
    os.chdir(on_folder_list.text)
    self.dir_tek = os.getcwd()
    self.off_folder_list()
    self.subdir = self.func_folder_list()
    self.on_folder_list()
    return
    
  # Отключение folder_list с экрана
  def off_folder_list(self):
      for i in range(len(self.subdir)):
        self.grd.remove_widget(self.button_folder_list_menu[i])
      return
  
  def create_folder(self):
    print('create_folder begin')
    self.ids.float_folder.add_widget(self.ids.popup_folder_box)
    folder_self_popupcf.popup_create_folder()