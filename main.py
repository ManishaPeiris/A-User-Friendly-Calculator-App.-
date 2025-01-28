from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Calculator(BoxLayout):
    def calculate(self, operation):
        try:
            # Get input numbers from TextInputs
            num1 = float(self.ids.num1_input.text)
            num2 = float(self.ids.num2_input.text)

            # Perform the calculation based on the operation
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 == 0:
                    result = "Error! Divide by Zero"
                else:
                    result = num1 / num2
            else:
                result = "Invalid Operation"

            # Display the result in the Label
            self.ids.result_label.text = f"Result: {result}"

        except ValueError:
            # Handle invalid input
            self.ids.result_label.text = "Please enter valid numbers!"


class CalculatorApp(App):
    def build(self):
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
