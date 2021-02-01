from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import time
import datetime
from faceRec import *
class TestApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        blue = (0, 0, 1.5, 2.5)
        
        btn =  Button(text='Take Attendance', background_color=blue, font_size=90)        
        btn.bind(on_press=self.callback)
        self.label = Label(text="Click to take Attendance", font_size='20sp')
        layout.add_widget(btn)
        layout.add_widget(self.label)
        return layout
    def callback(self, event):
        
        a,nam = take()
        if a == 1:
            date = datetime.date.today()
            time = datetime.datetime.now().strftime("%I:%M:%S %p")
            self.label.text = "Attendance of "+nam+" has taken at "+str(date)+" "+str(time)+"\nClick the above button again to take next attendance"
        else:
            self.label.text = "try again"

        

        
TestApp().run()
