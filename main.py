from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from evaluate import evlt, TooManyBracketsException, TooManyOperandsException, TooManyOperatorsException
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Rectangle, Color
import sys

# Popup class to instantiate the popup widget in kv language
# If we directly define a Popup widget in kv file,
# then during execution, the popup will always be open
# or, in clearer words, the kv language will automatically call open() method on program execution
class Popups(Popup):
    def __init__(self, message):
        self.message = message
        Popup.__init__(self)

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs) # lets you use methods for BoxLayout class object by initiating a boxlayout object as self
    def evl(self):
        try:
            # self.ids refers to all the ids defined in kv
            # self.ids.answer refers to the "widget" with answer id
            # self.ids.answer.text refers to its text attribute(property)
            self.ids.answer.text = str(int(evlt(self.ids.answer.text)))
        except OverflowError:
            # Creates a popups object (i.e. forms a popup widget to appear on the program)
            popup = Popups("Overflow! You only have 32 bits.")
            popup.open()
        except TooManyOperandsException:
            popup = Popups("Too bad operands don't go together very well!")
            popup.open()
        except TooManyBracketsException:
            popup = Popups("Pls check your brackets, doofus.")
            popup.open()
        except TooManyOperatorsException:
            popup = Popups("Too many operators!")
            popup.open()
        except:
            popup = Popups("Something weird happened.")
            popup.open()



class CalculatorApp(App):
    def build(self):
        return Calculator()

if __name__ == "__main__":
    CalculatorApp().run()