from kivy.uix.screenmanager import Screen
from kivy.properties import (StringProperty, ObjectProperty, ListProperty)
import popup as pf
import multiexpressionbutton as meb
from kivy.graphics import Color, Line
import os.path
from kivy.clock import Clock

file_testapp = globals()
file_testapp = ObjectProperty(None)
file_main = globals()
file_main = ObjectProperty(None)
file_popup = globals()
file_popup = ObjectProperty(None)
self_file = ObjectProperty(None)
#print('from file_menu gettattr:', getattr(self_test, '__name__'))


# Первое окно приложения.
class FileMenu(Screen):
  
  global self_main, subdir
  text_for_label = StringProperty("Список заметок")
  files_txt = ListProperty()
  float = ObjectProperty()
  scroll = ObjectProperty()
  grd = ObjectProperty()
  button_menu = ObjectProperty(None)
  popup_box = ObjectProperty()
  
  def __init__(self, **kwargs):
    super(FileMenu, self).__init__(**kwargs)
    global self_popup, self_main, subdir, self_file
    print("File_menu init")
    self_file = globals()
    self_file = self
    self_popup = pf
    self.send_self_file()
    #self.build_file_menu()
    return
    
  def send_self_file(self):
      pf.PopupFile.receive_self_file_menu_in_popup(self, self_file)
      
  def receive_self_testapp_in_file_menu(self,self_testapp):
      global file_testapp
      file_testapp = self_testapp
  
  def receive_self_main_in_file_menu(self, self_main):
      global file_main
      file_main = self_main
      
  def receive_self_popup_in_file_menu(self, self_popup):
      global file_popup
      file_popup = self_popup
      
  def build_file_menu(self):
    global subdir, self_main, self_popup, grd, s_man
    print("build_file_menu begin")
    grd = self_file.grd
    grd = self_file.file_list_building(grd)
    self_file.grd.bind(minimum_height = self_file.grd.setter('height'))
    self_file.is_popup = True
    Clock.schedule_once(self_file.shed_label, 3)
    print("build_file_menu end!")
    return

  def choice_file_main(self, file_list_building):
    global self_testapp, file_main
    print("choice_file_main begin")
    file_testapp.sm.current = 'text_area'
    file_main.choice_file_mainlay(file_list_building)
    return
    
  def button_plus_pressed(self):
    global self_testapp
    print("button '+' pressed")
    file_testapp.sm.current = 'text_area'
    file_main.create_file_building()
    file_main.text_area.focus = True
    return
    
#  def on_text_for_label(self, *args):
#    print('label changed')

# Файловая функция
# читаем файлы в список self.files_txt
# вызываем из file_list_building
  def func_file_list(self):
    global subdir
    subdir = os. getcwd()
    if subdir:
      #print("subdir:", subdir)
      os.chdir(subdir)
    file_list = os.listdir()
    self.files_txt = []
    for i in file_list:
      if ".txt" in i:
        self.files_txt.append(i)
    return self.files_txt
    
# Включение file_list.
  def file_list_building(self, grd):
    print("file_list_building begin")
    grd.clear_widgets()
    #grd.padding = (10, 10, 10, 10)
    self.grd.row_force_default = True
    self.grd.row_default_height = 170
    self.grd.spacing_vertical = 2
    self.files_txt = self.func_file_list()
    self.button_list_menu = []
    self.files_txt.sort()
    for i in range(len(self.files_txt)):
      self.button_list_menu.append(i)
      self.button_list_menu[i] = meb.MultiExpressionButton(
        text = self.files_txt[i],
        background_color = (0, 0, 0, 1),
        text_size = (1000, 50),
        halign = 'left' )
      y_line = 50
      with self.grd.canvas.after:
        Color(1, 1, 1)
        y_line += i * self.grd.row_default_height + self.grd.spacing_vertical * i * 0.6
        Line(
          points=[ 0, y_line, 1100, y_line ],
          width = 1 )
      self.button_list_menu[i].bind(on_single_press = self.choice_file_main)
      self.button_list_menu[i].bind(on_long_press = file_popup.popup_file)
      self.grd.add_widget(self.button_list_menu[i])
    print('Всего файлов', len(self.files_txt))
    return self.grd

  def shed_label(self, time):
    print('shed_label begin. time: ', time)
    #self.text_for_label = "Список заметок"
    if (len(self.files_txt) == 0):
    #and (self.back_from_ml == False):
      self.ids.label_app.text = 'В этой папке заметок нет. Нажми +, чтобы добавить, или = для выбора папки.'
    else:
      self.ids.label_app.text = 'Список заметок'
      
  # Выключение file_list с экрана
  def off_file_list(self):
    for i in range(len(self.files_txt)):
      self.grd.remove_widget(self.button_list_menu[i])
    return
  
