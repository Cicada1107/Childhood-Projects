#Calculator using kivy in python
#5


#fix the input screen getting cleared when it runs out of space.


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (365, 602)

Builder.load_file('calc.kv')

operators = ["+", "%", "-", "/", "x"]

class MyLayout(Widget):
    """Marks the app's layout"""

    def clear_screen(self):
        """Clears the calculator screen"""
        self.ids.calc_input.text = ''

    def clear(self):
        """Equivalent of backspace"""
        prior = self.ids.calc_input.text
        if prior != 0:
            self.ids.calc_input.text = prior[0:-1]
            if self.ids.calc_input.text == '': self.ids.calc_input.text = '0'

    def enter_digit(self, digit: str):
        """Enters the pressed digit into the screen"""
        if self.ids.calc_input.text == '0': self.clear_screen()
        self.ids.calc_input.text += str(digit)

    def funct(self, operator):
        """Puts operator functions in the calculator"""
        prior = self.ids.calc_input.text
        if operator == ".":
            if "." in prior: pass
            else:
                if prior != "" and prior[-1] not in operators: self.ids.calc_input.text += str(operator)
                else: pass
        else:
            if prior != '' and prior[-1] not in operators: self.ids.calc_input.text += str(operator)
            else: pass
        
    def change_sign(self):  #fix this
        """Changes the sign of number on the screen"""
        prior = self.ids.calc_input.text
        if prior[0] != 0:
            if prior[0] == "-": self.ids.calc_input.text = prior[1:]
            else: self.ids.calc_input.text = "{}{}".format("-", prior)

    def equals(self):
        prior = self.ids.calc_input.text
        try: answer = str(self.calculate(prior))
        except: answer = "Error"
        self.ids.calc_input.text = answer           

    def calculate(self, expression):
        """Calculates the result of a given expression conatining operators."""
        answer = eval(expression)
        return answer 


class CalculatorApp(App):
    """The calculator app"""
    
    def build(self):
        """Builds the app"""
        return MyLayout()

CalculatorApp().run()
