from kivy.base import runTouchApp
from kivy.clock import Clock
from kivy.factory import Factory

class LongpressButton(Factory.Button):
    __events__ = ('on_long_press', )

    long_press_time = Factory.NumericProperty(1)
    
    def on_state(self, instance, value):
        if value == 'down':
            lpt = self.long_press_time
            self._clockev = Clock.schedule_once(self._do_long_press, lpt)
        else:
            self._clockev.cancel()

    def _do_long_press(self, dt):
        self.dispatch('on_long_press')
        
    def on_long_press(self, *largs):
        pass
        
    def press(self):
        print("simple press")
      
    def long_press(self):
        print("long press")
        
btn = LongpressButton(
            long_press_time=0.5,
            on_press= lambda w: setattr(w, 'text', 'short press!'),
            on_long_press= lambda w: setattr(w, 'text', 'long press!'))
            


runTouchApp(btn)