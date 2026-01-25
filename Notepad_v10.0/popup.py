from kivy.uix.boxlayout import BoxLayout
from kivy.properties import (ObjectProperty, BooleanProperty)
from kivy.clock import Clock
import file_menu as fm
import os.path

popup_testapp = globals()
popup_testapp = ObjectProperty(None)
self_popup = globals()
self_popup = ObjectProperty(None)


class PopupFile(BoxLayout):
  
  box = ObjectProperty()
  box_open = ObjectProperty()
  box_delete = ObjectProperty()
  box_close = ObjectProperty()
  is_popup = BooleanProperty(True)

  def __init__(self, **kwargs):
    super(PopupFile, self).__init__(**kwargs)
    print("PopupFile init")
    
    global file_fun, self_popup, s_man, popup_testapp
    self_popup = self
    self.send_self_popup()
    self.file = fm.FileMenu
    
  def send_self_popup(self):
      self_popup = globals()
      self_popup = self
      fm.FileMenu.receive_self_popup_in_file_menu(self, self_popup)
      
  def receive_self_testapp_in_popup(self, self_testapp):
      global popup_testapp
      popup_testapp = self_testapp
      
  def receive_self_file_menu_in_popup(self, self_file):
      global popup_file_menu
      popup_file_menu = self_file
      
  def is_popup_in_float(self):
    for child in popup_file_menu.float.children:
      if child == popup_file_menu.popup_box:
        print("box in float!")
        return True
      else:
        print("box not in float!")
        return False

  def popup_file(self, file_list_building):
    print("popup_file begin. Long press detected.")
    global file_list_obj, s_man, selfy_file
    print("is_popup:", self.is_popup)
    if not self.is_popup_in_float():
      popup_file_menu.float.add_widget(popup_file_menu.ids.popup_box)
      #print('выполнено add_widget')
    file_list_obj = file_list_building
    self.box.opacity = 1
    self.box_open.size_hint_y = 0.25
    self.box_delete.size_hint_y = 0.25
    self.box_close.size_hint_y = 0.25
    self.file.files_txt = fm.FileMenu.func_file_list(self)
    for i in range(len(self.file.files_txt)):
      popup_file_menu.button_list_menu[i].unbind(on_long_press = self.popup_file)
    return

  def popup_close(self):
    print("popup close begin")
    if self.is_popup_in_float():
      popup_file_menu.float.remove_widget(popup_file_menu.popup_box)
    self.box.opacity = 0
    self.box_open.size_hint_y = None
    self.box_open.height = '0dp'
    self.box_delete.size_hint_y = None
    self.box_delete.height = '0dp'
    self.box_close.size_hint_y = None
    self.box_close.height = '0dp'
    self.file.files_txt = self.file.func_file_list(self)
    for i in range(len(self.file.files_txt)):
      popup_file_menu.button_list_menu[i].unbind(on_long_press = self.popup_file)
    Clock.schedule_once(self.file.build_file_menu, 0.6)
    return

  def popup_open(self):
    global file_list_obj
    self.is_popup = False
    file_list_building = file_list_obj
    popup_file_menu.choice_file_main(file_list_building)
    if self.is_popup_in_float():
      popup_file_menu.float.remove_widget(self.box)
    return

  def popup_delete(self):
    global file_list_obj
    self.is_popup = False
    os.remove(file_list_obj.text)
    popup_file_menu.text_for_label = f"{file_list_obj.text} удален!"
    print("file deleted!")
    popup_testapp.sm.get_screen('menu_file').build_file_menu()
    if self.is_popup_in_float():
      popup_testapp.sm.get_screen('menu_file').float.remove_widget(self.box)
    return