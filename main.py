from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from evaluate import evlt

# Popup class to instantiate the popup widget in kv language
# If we directly define a Popup widget in kv file,
# then during execution, the popup will always be open
# or, in clearer words, the kv language will automatically call open() method on program execution
class Popups(Popup):
    pass

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # lets you use methods for BoxLayout class object by initiating a boxlayout object as self
    def evl(self):
        try:
            # self.ids refers to all the ids defined in kv
            # self.ids.answer refers to the "widget" with answer id
            # self.ids.answer.text refers to its text attribute(property)
            self.ids.answer.text = str(int(evlt(self.ids.answer.text)))
        except:
            # Creates a popups object (i.e. forms a popup widget to appear on the program)
            popup = Popups()
            popup.open()


class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()