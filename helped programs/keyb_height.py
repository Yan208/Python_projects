from kivy.app import App
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.utils import platform
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
if platform == 'android':
    from jnius import autoclass

class MyTextInput(TextInput):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # User can change keyboard size during input, so we should regularly update the keyboard height
        self.trigger_keyboard_height = Clock.create_trigger(self.update_keyboard_height, 0.2, interval=True)
        self.trigger_cancel_keyboard_height = Clock.create_trigger(lambda dt: self.trigger_keyboard_height.cancel(), 1.0, interval=False)
    def update_keyboard_height(self, dt):
        if platform=='android':
            App.get_running_app().keyboard_height = self.get_android_vkeyboard_height()
    def _bind_keyboard(self):
        super()._bind_keyboard()
        if platform=='android':
            self.trigger_cancel_keyboard_height.cancel()
            self.trigger_keyboard_height()
    def _unbind_keyboard(self):
        super()._unbind_keyboard()
        if platform=='android':
            self.trigger_cancel_keyboard_height()

    def get_android_vkeyboard_height(self):
        if platform=='android':
            Activity = autoclass('org.kivy.android.PythonActivity').mActivity
            Rect = autoclass('android.graphics.Rect')
            root_window = Activity.getWindow()
            view = root_window.getDecorView()
            r = Rect()
            view.getWindowVisibleDisplayFrame(r)
            return Window.height-(r.bottom-r.top)
        
class MyPopup(Popup): # Popup, which is shifted up when overlapped by virtual keyboard
    def on_open(self):
        App.get_running_app().fbind('keyboard_height', self._align_center)
    def _align_center(self, *l):
        if self._window:
            self.center = (self._window.center[0], self._window.center[1] + max(App.get_running_app().keyboard_height-(self._window.height-self.height)/2, 0))

kv = '''
#:import Factory kivy.factory.Factory
FloatLayout:
    MyTextInput:
        text: ' '.join([str(i) for i in range(500)])
        size_hint: (0.9, 0.55-max(app.keyboard_height/root.height - 0.2, 0.0))
        pos_hint: {'x': 0.05, 'y': max(app.keyboard_height/root.height, 0.2)}
    Button:
        text: 'Open popup'
        size_hint: (0.2, 0.1)
        pos_hint: {'x': 0.4, 'y': 0.8}
        on_press: Factory.MyPopup().open()
<MyPopup>:
    auto_dismiss: True
    title: 'Some popup'
    size_hint: (0.8,0.6)
    AnchorLayout:
        MyTextInput:
            size_hint: (0.8, 0.2)
            multiline: False
        '''

class Sample(App):
    keyboard_height = NumericProperty(0)
    
    def build(self):
        return Builder.load_string(kv)

Sample().run()
