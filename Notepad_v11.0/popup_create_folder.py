'''
Docstring for popup_create_folder
Создать папку при нажатии на +.
'''
import os
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
import foldermenu as foldermen
#from kivy.app import App

popup_folder = globals()
popup_folder = ObjectProperty(None)
self_popup_create_folder = globals()
self_popup_create_folder = ObjectProperty(None)

class PopupCreateFolder(BoxLayout):
    '''
    Docstring for PopupCreateFolder
    '''
    print('begin class PopupCreateFolder')

    box_create_folder = ObjectProperty()
    float_folder = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("PopupCreateFolder init")
        global self_popup_create_folder
        self_popup_create_folder = self
        #self.app = App.get_running_app()
        self.send_self_popup_create_folder()

    def send_self_popup_create_folder(self):
        #self_popup_create_folder = globals()
        #self_popup_create_folder = self
        foldermen.FolderMenu.receive_self_popupcf_in_folder_menu(self, self_popup_create_folder=self)
      
    def receive_self_folder_menu_in_popup_cr_folder(self, self_folder):
        global popup_folder
        popup_folder = self_folder
      
      
    def popup_create_folder(self):
        print("popup_create_folder begin. Button + pressed in folder.")
      
      
    def create_folder_cancel(self):
        print('create_folder_cancel begin')
        popup_folder.ids.float_folder.remove_widget(popup_folder.ids.popup_folder_box)
      
    def create_folder_ok(self):
        print('create_folder_ok begin')
        print('имя папки:', self.ids.text_create_folder.text)
        os.mkdir(self.ids.text_create_folder.text)
        popup_folder.build_folder_menu()
        
        popup_folder.ids.float_folder.remove_widget(popup_folder.ids.popup_folder_box)
