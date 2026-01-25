# Notepad v10.00
# оптимизация в классы

from kivy.config import Config
Config.set('kivy', 'keyboard_mode', '')
from kivy.uix.screenmanager import ScreenManager, NoTransition
from kivy.properties import (StringProperty, ObjectProperty)
import file_menu as fm
import mainlay as ml
import os.path
from kivymd.app import MDApp
import popup as popup
import foldermenu as foldermenu
#import popup_create_folder as popup_create_folder

print('before global')
self_testapp = globals()
self_testapp = ObjectProperty(None)
subdir = StringProperty(os. getcwd())
file_list_obj = ObjectProperty()


class MainApp(MDApp):
  '''
  Docstring для MainApp

  '''
  sm = ObjectProperty(ScreenManager( transition=NoTransition()))
  
  def __init__(self, **kwargs):
    super(MainApp, self).__init__(**kwargs)
    print('MainApp init')
    self.title = 'My Notepad'
    global self_testapp
    self_testapp = self
    self.send_self_testapp()
    self.sm = ScreenManager( transition=NoTransition())
    
  def send_self_testapp(self):
      '''
      Docstring для send_self_testapp
      
      :param self: Описание
      передает self в другие .py файлы
      '''
      fm.FileMenu.receive_self_testapp_in_file_menu(self, self_testapp)
      popup.PopupFile.receive_self_testapp_in_popup(self, self_testapp)
      foldermenu.FolderMenu.receive_self_testapp_in_folder_menu(self, self_testapp)
      ml.MainLayout.receive_self_testapp_in_mainlay(self, self_testapp)
      
  def build(self):
    '''
    Docstring для build
    размещаем на экране список файлов и создаем другие экраны
    '''
    print('build begin')
    self.sm.add_widget(fm.FileMenu(name='menu_file'))
    self.sm.add_widget(ml.MainLayout(name='text_area'))
    self.sm.add_widget(foldermenu.FolderMenu(name='menu_folder'))
    self.theme_cls.theme_style = "Dark"
    self.theme_cls.primary_palette = "Orange"
    self.sm.get_screen('menu_file').build_file_menu()
    print('build end')
    return self.sm

if __name__ == "__main__":
  app = MainApp()
  app.run()