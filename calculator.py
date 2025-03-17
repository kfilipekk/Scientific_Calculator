import math
import cmath
import matplotlib.pyplot as plt
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
        }

    def clear(self):
        self.current = "0"
        self.operation = None
        self.previous = None
        return self.current

    def clear_entry(self):
        self.current = "0"
        return self.current

    def memory_store(self):
        try:
            self.memory = float(self.current)
        except ValueError:
            pass
        return self.current

    def memory_recall(self):
        self.current = str(self.memory)
        return self.current

    def memory_clear(self):
        self.memory = 0.0
        return self.current

    def memory_add(self):
        try:
            self.memory += float(self.current)
        except ValueError:
            pass
        return self.current

    def memory_subtract(self):
        try:
            self.memory -= float(self.current)
        except ValueError:
            pass
        return self.current

    def toggle_angle_mode(self):
        self.is_radians = not self.is_radians
        return "RAD" if self.is_radians else "DEG"

    def evaluate(self):
        if self.previous is None or self.operation is None:
            return self.current
        try:
            prev = complex(self.previous) if "j" in self.previous else float(self.previous)
            curr = complex(self.current) if "j" in self.current else float(self.current)
            if self.operation == "+":
                result = prev + curr
            elif self.operation == "-":
                result = prev - curr
            elif self.operation == "*":
                result = prev * curr
            elif self.operation == "/":
                result = prev / curr if curr != 0 else "Error"
            elif self.operation == "^":
                result = prev ** curr
            elif self.operation == "mod":
                result = prev % curr if curr != 0 else "Error"
            else:
                result = self.current
            self.current = str(result)
            self.history.append(f"{self.previous} {self.operation} {curr} = {result}")
            self.previous = None
            self.operation = None
            return self.current
        except Exception:
            return "Error"

    def scientific_operation(self, op):
        try:
            value = complex(self.current) if "j" in self.current else float(self.current)
            if isinstance(value, complex):
                if op == "sin": result = cmath.sin(value)
                elif op == "cos": result = cmath.cos(value)
                elif op == "tan": result = cmath.tan(value)
                elif op == "sqrt": result = cmath.sqrt(value)
                elif op == "exp": result = cmath.exp(value)
                else: result = value
            else:
                if op == "sin":
                    result = math.sin(value) if self.is_radians else math.sin(math.radians(value))
                elif op == "cos":
                    result = math.cos(value) if self.is_radians else math.cos(math.radians(value))
                elif op == "tan":
                    result = math.tan(value) if self.is_radians else math.tan(math.radians(value))
                elif op == "asin":
                    result = math.asin(value) if self.is_radians else math.degrees(math.asin(value))
                elif op == "acos":
                    result = math.acos(value) if self.is_radians else math.degrees(math.acos(value))
                elif op == "atan":
                    result = math.atan(value) if self.is_radians else math.degrees(math.atan(value))
                elif op == "log":
                    result = math.log10(value)
                elif op == "ln":
                    result = math.log(value)
                elif op == "sqrt":
                    result = math.sqrt(value)
                elif op == "exp":
                    result = math.exp(value)
                elif op == "pi":
                    result = math.pi
                elif op == "e":
                    result = math.e
                elif op == "sinh":
                    result = math.sinh(value)
                elif op == "cosh":
                    result = math.cosh(value)
                elif op == "tanh":
                    result = math.tanh(value)
                else:
                    result = value
            self.current = str(result)
            return self.current
        except Exception:
            return "Error"

    def append_digit(self, digit):
        if self.current in ("0", "Error"):
            self.current = digit
        else:
            self.current += digit
        return self.current

    def append_decimal(self):
        if "." not in self.current:
            self.current += "."
        return self.current

    def append_complex(self):
        self.current += "j"
        return self.current

    def set_operation(self, op):
        if self.current != "Error":
            self.previous = self.current
            self.operation = op
            self.current = "0"
        return self.current

    def negate(self):
        try:
            self.current = str(-float(self.current))
        except ValueError:
            pass
        return self.current

    def percent(self):
        try:
            self.current = str(float(self.current) / 100)
        except ValueError:
            pass
        return self.current

    def factorial(self):
        try:
            value = int(float(self.current))
            if value >= 0:
                self.current = str(math.factorial(value))
            else:
                self.current = "Error"
        except Exception:
            self.current = "Error"
        return self.current

    def convert_unit(self, conversion):
        try:
            value = float(self.current)
            self.current = str(self.unit_conversions[conversion](value))
            return self.current
        except Exception:
            return "Error"

    def graph_function(self, func):
        try:
            x = np.linspace(-10, 10, 400)
            if func == "sin":
                y = np.sin(x) if self.is_radians else np.sin(np.radians(x))
            elif func == "cos":
                y = np.cos(x) if self.is_radians else np.cos(np.radians(x))
            elif func == "tan":
                y = np.tan(x) if self.is_radians else np.tan(np.radians(x))
            else:
                return
            plt.plot(x, y, label=func)
            plt.title(f"Graph of {func}(x)")
            plt.xlabel("x")
            plt.ylabel(f"{func}(x)")
            plt.grid(True)
            plt.legend()
            plt.show()
        except Exception:
            pass

    def get_history(self):
        return "\n".join(self.history) if self.history else "No history"