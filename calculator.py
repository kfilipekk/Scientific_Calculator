import math
import cmath
import numpy as np

class CalculatorLogic:
    def __init__(self):
        self.memory = 0.0
        self.current = "0"
        self.operation = None
        self.previous = None
        self.is_radians = True
        self.history = []
        self.unit_conversions = {
            "m_to_cm": lambda x: x * 100,
            "cm_to_m": lambda x: x / 100,
            "kg_to_g": lambda x: x * 1000,
            "g_to_kg": lambda x: x / 1000,
            "c_to_f": lambda x: (x * 9/5) + 32,
            "f_to_c": lambda x: (x - 32) * 5/9,
            "km_to_m": lambda x: x * 1000,
            "m_to_km": lambda x: x / 1000,
        }
        self.constants = {
            "π": math.pi,
            "e": math.e,
            "c": 299792458,  # Speed of light in m/s
            "g": 9.80665,    # Acceleration due to gravity in m/s²
        }

    def clear(self):
        """Clears the current calculation."""
        self.current = "0"
        self.operation = None
        self.previous = None
        return self.current

    def clear_entry(self):
        """Clears the current entry."""
        self.current = "0"
        return self.current

    def memory_clear(self):
        """Clears the memory."""
        self.memory = 0.0
        return self.current

    def memory_recall(self):
        """Recalls the memory value."""
        self.current = str(self.memory)
        return self.current

    def memory_add(self):
        """Adds the current value to memory."""
        try:
            self.memory += float(self.current)
        except ValueError:
            pass
        return self.current

    def memory_subtract(self):
        """Subtracts the current value from memory."""
        try:
            self.memory -= float(self.current)
        except ValueError:
            pass
        return self.current

    def memory_store(self):
        """Stores the current value in memory."""
        try:
            self.memory = float(self.current)
        except ValueError:
            pass
        return self.current

    def append_digit(self, digit):
        """Appends a digit to the current value."""
        if self.current == "0":
            self.current = digit
        else:
            self.current += digit
        return self.current

    def append_decimal(self):
        """Appends a decimal point to the current value."""
        if "." not in self.current:
            self.current += "."
        return self.current

    def negate(self):
        """Negates the current value."""
        if self.current.startswith("-"):
            self.current = self.current[1:]
        else:
            self.current = "-" + self.current
        return self.current

    def percent(self):
        """Converts the current value to a percentage."""
        try:
            self.current = str(float(self.current) / 100)
        except ValueError:
            pass
        return self.current

    def append_complex(self):
        """Appends 'j' for complex numbers."""
        self.current += "j"
        return self.current

    def set_operation(self, op):
        """Sets the operation and stores the previous value."""
        if self.previous is None:
            try:
                self.previous = float(self.current) if "j" not in self.current else complex(self.current)
            except ValueError:
                self.previous = self.current
        elif self.operation:
            self.evaluate()
        self.operation = op
        self.current = "0"
        return self.current

    def evaluate(self):
        """Evaluates the current expression."""
        if self.previous is not None and self.operation:
            try:
                curr = float(self.current) if "j" not in self.current else complex(self.current)
                prev = self.previous
                if self.operation == "+":
                    result = prev + curr
                elif self.operation == "-":
                    result = prev - curr
                elif self.operation == "*":
                    result = prev * curr
                elif self.operation == "/":
                    if curr == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = prev / curr
                elif self.operation == "^":
                    result = prev ** curr
                elif self.operation == "mod":
                    result = prev % curr
                self.history.append(f"{prev} {self.operation} {curr} = {result}")
                self.current = str(result)
                self.previous = None
                self.operation = None
            except Exception as e:
                self.current = "Error"
                self.previous = None
                self.operation = None
        return self.current

    def scientific_operation(self, op):
        """Performs a scientific operation on the current value."""
        try:
            value = float(self.current) if "j" not in self.current else complex(self.current)
            angle_func = lambda x: x if self.is_radians else math.radians(x)
            if op == "sin":
                result = math.sin(angle_func(value)) if isinstance(value, (int, float)) else cmath.sin(value)
            elif op == "cos":
                result = math.cos(angle_func(value)) if isinstance(value, (int, float)) else cmath.cos(value)
            elif op == "tan":
                result = math.tan(angle_func(value)) if isinstance(value, (int, float)) else cmath.tan(value)
            elif op == "sinh":
                result = math.sinh(value) if isinstance(value, (int, float)) else cmath.sinh(value)
            elif op == "cosh":
                result = math.cosh(value) if isinstance(value, (int, float)) else cmath.cosh(value)
            elif op == "tanh":
                result = math.tanh(value) if isinstance(value, (int, float)) else cmath.tanh(value)
            elif op == "asin":
                result = math.asin(value) if isinstance(value, (int, float)) else cmath.asin(value)
            elif op == "acos":
                result = math.acos(value) if isinstance(value, (int, float)) else cmath.acos(value)
            elif op == "atan":
                result = math.atan(value) if isinstance(value, (int, float)) else cmath.atan(value)
            elif op == "log":
                result = math.log10(value) if isinstance(value, (int, float)) else cmath.log10(value)
            elif op == "ln":
                result = math.log(value) if isinstance(value, (int, float)) else cmath.log(value)
            elif op == "sqrt":
                result = math.sqrt(value) if isinstance(value, (int, float)) else cmath.sqrt(value)
            elif op == "exp":
                result = math.exp(value) if isinstance(value, (int, float)) else cmath.exp(value)
            self.current = str(result)
        except Exception:
            self.current = "Error"
        return self.current

    def factorial(self):
        """Calculates the factorial of the current value."""
        try:
            value = int(float(self.current))
            if value < 0:
                self.current = "Error"
            else:
                self.current = str(math.factorial(value))
        except ValueError:
            self.current = "Error"
        return self.current

    def toggle_angle_mode(self):
        """Toggles between radians and degrees."""
        self.is_radians = not self.is_radians
        return "RAD" if self.is_radians else "DEG"

    def convert_unit(self, conversion):
        """Converts the current value using the specified unit conversion."""
        try:
            value = float(self.current)
            result = self.unit_conversions[conversion](value)
            self.current = str(result)
        except ValueError:
            self.current = "Error"
        return self.current

    def insert_constant(self, constant):
        """Inserts a constant into the current value."""
        self.current = str(self.constants[constant])
        return self.current

    def get_history(self):
        """Returns the calculation history."""
        return "\n".join(self.history) if self.history else "No history"

    def evaluate_function(self, func_str, x):
        """Safely evaluates a user-defined function for a given x."""
        try:
            safe_dict = {
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log10,
                'ln': math.log,
                'sqrt': math.sqrt,
                'exp': math.exp,
                'pi': math.pi,
                'e': math.e,
                'x': x,
            }
            return eval(func_str, {"__builtins__": None}, safe_dict)
        except Exception as e:
            raise ValueError(f"Invalid function: {e}")

    def graph_function(self, func_str, x_min, x_max, num_points=400):
        """Graphs the user-defined function over the specified range."""
        try:
            x_values = np.linspace(x_min, x_max, num_points)
            y_values = [self.evaluate_function(func_str, x) for x in x_values]
            return x_values, y_values
        except Exception as e:
            raise ValueError(f"Error plotting function: {e}")