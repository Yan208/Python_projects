'''
Docstring for Notepad_v11.0.foldermenu
Действия для вывода списка папок.
'''
import os
from kivy.uix.screenmanager import Screen
from kivy.properties import (StringProperty, ObjectProperty) # pylint: disable=import-error,no-name-in-module
from kivy.uix.button import Button
from kivy.app import App
import popup_create_folder as pfolder
import file_menu as fm

#folder_testapp = globals()
#folder_testapp = ObjectProperty(None)
self_folder = globals()
self_folder = ObjectProperty(None)
folder_self_popupcf = globals()
folder_self_popupcf = ObjectProperty(None)

class FolderMenu(Screen):
    '''
    Docstring for FolderMenu
    Класс для вывода списка папок.
    '''
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
        self.folder_list = []
        self.button_folder_list_menu = []
        #self.subdir

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

    def on_folder_list(self):
        '''
        Docstring for on_folder_list
        Включение folder_list на экран
        :param self: Description
        '''
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

    def func_folder_list(self):
        '''
        Docstring for func_folder_list
        читаем список папок в subdir
        :param self: Description
        '''
        #all_list = os.listdir()
        self.folder_list = []
        self.dir_tek = os.getcwd()
        print('tek dir from func_folder_list:', self.dir_tek)
        example_dir = self.dir_tek
        #'/storage/emulated/0/Documents/Pydroid3'
        with os.scandir(example_dir) as files:
            subdir = [file.name for file in files if file.is_dir()]
            subdir.insert(0, "..")
        return subdir

    def choice_folder(self, on_folder_list):
        '''
        Docstring for choice_folder
        Файловая функция.
        Как choice_file, только для folder
        :param self: Description
        :param on_folder_list: Description
        '''
        print("choice_folder")
        print("Пытаемся перейти в:", on_folder_list.text)
        print("Текущий рабочий каталог:", os.getcwd())
        os.chdir(on_folder_list.text)
        self.dir_tek = os.getcwd()
        self.off_folder_list()
        self.subdir = self.func_folder_list()
        self.on_folder_list()

    def off_folder_list(self):
        '''
        Docstring for off_folder_list
        Отключение folder_list с экрана
        :param self: Description
        '''
        for i in range(len(self.subdir)):
            self.grd.remove_widget(self.button_folder_list_menu[i])

    def create_folder(self):
        print('create_folder begin')
        self.ids.float_folder.add_widget(self.ids.popup_folder_box)
        folder_self_popupcf.popup_create_folder()
