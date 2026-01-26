#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
   Code to demonstrate the different events that can be done with the multiexpressionbutton object.
"""
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import multiexpressionbutton as meb

__author__ = "Mark Rauch Richards"


class MainWindow(GridLayout):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 8
        # multiEb ))
        button = meb.MultiExpressionButton(text="Click ME")
        button.bind(on_long_press=self.long_action)
        button.bind(on_single_press=self.single_action)
        button.bind(on_double_press=self.double_action)
        self.add_widget(button)

    #@staticmethod
    def long_action(self, instance):
        button2 = Button (
          text = "long"  )
        self.add_widget(button2)
        print('long press')

    #@staticmethod
    def single_action(self, instance):
        button1 = Button (
          text = "single"  )
        self.add_widget(button1)
        print('single press')

    #@staticmethod
    def double_action(self, instance):
        button3 = Button (
          text = "double"  )
        self.add_widget(button3)
        print('double press')


class Testbutton(App):
    def build(self):
        self.title = 'Test'
        main = MainWindow()
        return main


if __name__ == '__main__':
    Testbutton().run()