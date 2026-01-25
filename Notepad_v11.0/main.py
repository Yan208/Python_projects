'''
Docstring
Notepad v11.00
'''
# оптимизация в классы
__version__ = '11.0'

import os
import sys
from kivy.config import Config
from kivy.uix.screenmanager import ScreenManager, NoTransition
# здесь линтер срабатывает ложно, оставить!
from kivy.properties import StringProperty, ObjectProperty


if sys.platform.startswith('win'):
    Config.set('graphics', 'width', '1100')
    Config.set('graphics', 'height', '600')
    #Config.set('graphics', 'resizable', '0')
    Config.set('graphics', 'position', 'auto')  # Центрирование окна
if sys.platform.startswith('android'):
    Config.set('kivy', 'keyboard_mode', '')

# здесь линтер срабатывает ложно, оставить!
from kivymd.app import MDApp
import file_menu as fm
import mainlay as ml
#import popup
import foldermenu


#import popup_create_folder as popup_create_folder

print('before global')

subdir = StringProperty(os. getcwd())
file_list_obj = ObjectProperty()


class MainApp(MDApp):
    '''
    Docstring для MainApp
    Приложение блокнот.

    '''
    print('begin class MainApp')
    sm = ObjectProperty(ScreenManager( transition=NoTransition()))
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print('MainApp init')
        self.title = 'My Notepad'
        self.sm = ScreenManager( transition=NoTransition())
        path = "Notes"  # имя папки (в текущей директории)
        try:
            if not os.path.exists("Notes"):
                os.mkdir(path)
            print(f"Папка '{path}' создана успешно.")
            os.chdir(path)
        except FileExistsError:
            print(f"Папка '{path}' уже существует.")
            if os.path.exists("Notes"):
                print('Notes есть в папке')
                os.chdir(path)
        except PermissionError:
            print(f"Нет прав для создания папки '{path}'.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")

    def build(self): #0
        '''
        Docstring для build
        размещаем на экране список файлов и создаем другие экраны.
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
