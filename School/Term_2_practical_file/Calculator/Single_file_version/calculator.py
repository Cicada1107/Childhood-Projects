#Calculator using kivy in python

#this version is supposed to do away with the kivy file entirely by binding that code to the python format.


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (365, 602)

#Builder.load_file('calc.kv')

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

        layout = GridLayout(cols = 4, rows = 5)

        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "^", on_press = MyLayout.funct("**")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "CE", on_press = MyLayout.clear_screen()))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "C", on_press = MyLayout.clear("**")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "/", on_press = MyLayout.funct("/")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "7", on_press = MyLayout.enter_digit("7"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "8", on_press = MyLayout.enter_digit("8"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "9", on_press = MyLayout.enter_digit("9"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "x", on_press = MyLayout.funct("*")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "4", on_press = MyLayout.enter_digit("4"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "5", on_press = MyLayout.enter_digit("5"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "6", on_press = MyLayout.enter_digit("6"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "-", on_press = MyLayout.funct("-")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "1", on_press = MyLayout.enter_digit("1"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "2", on_press = MyLayout.enter_digit("2"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "3", on_press = MyLayout.enter_digit("3"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "+", on_press = MyLayout.funct("+")))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "+/-", on_press = MyLayout.change_sign(), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "0", on_press = MyLayout.enter_digit("0"), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = ".", on_press = MyLayout.funct("."), background_color = (157/255, 157/255, 157/255, 1)))
        layout.add_widget(Button(size_hint = (.2, .2), font_size = 32, text = "+", on_press = MyLayout.equals()))

        return MyLayout.layout

CalculatorApp().run()
