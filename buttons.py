##buttons.py
import tkinter as tk
from tkinter import ttk

class CalculatorButtons:
    def __init__(self, parent, display, logic):
        self.display = display
        self.logic = logic
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=1, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        self.create_buttons()

    def create_buttons(self):
        """Creates and lays out all calculator buttons."""
        button_layout = [
            ("MC", self.logic.memory_clear, 0, 0), ("MR", self.logic.memory_recall, 0, 1),
            ("M+", self.logic.memory_add, 0, 2), ("M-", self.logic.memory_subtract, 0, 3),
            ("MS", self.logic.memory_store, 0, 4),
            ("sin", lambda: self.logic.scientific_operation("sin"), 1, 0),
            ("cos", lambda: self.logic.scientific_operation("cos"), 1, 1),
            ("tan", lambda: self.logic.scientific_operation("tan"), 1, 2),
            ("sinh", lambda: self.logic.scientific_operation("sinh"), 1, 3),
            ("cosh", lambda: self.logic.scientific_operation("cosh"), 1, 4),
            ("asin", lambda: self.logic.scientific_operation("asin"), 2, 0),
            ("acos", lambda: self.logic.scientific_operation("acos"), 2, 1),
            ("atan", lambda: self.logic.scientific_operation("atan"), 2, 2),
            ("tanh", lambda: self.logic.scientific_operation("tanh"), 2, 3),
            ("π", lambda: self.logic.insert_constant("π"), 2, 4),
            ("log", lambda: self.logic.scientific_operation("log"), 3, 0),
            ("ln", lambda: self.logic.scientific_operation("ln"), 3, 1),
            ("√", lambda: self.logic.scientific_operation("sqrt"), 3, 2),
            ("e^x", lambda: self.logic.scientific_operation("exp"), 3, 3),
            ("e", lambda: self.logic.insert_constant("e"), 3, 4),
            ("7", lambda: self.logic.append_digit("7"), 4, 0),
            ("8", lambda: self.logic.append_digit("8"), 4, 1),
            ("9", lambda: self.logic.append_digit("9"), 4, 2),
            ("/", lambda: self.logic.set_operation("/"), 4, 3),
            ("C", self.logic.clear, 4, 4),
            ("4", lambda: self.logic.append_digit("4"), 5, 0),
            ("5", lambda: self.logic.append_digit("5"), 5, 1),
            ("6", lambda: self.logic.append_digit("6"), 5, 2),
            ("*", lambda: self.logic.set_operation("*"), 5, 3),
            ("CE", self.logic.clear_entry, 5, 4),
            ("1", lambda: self.logic.append_digit("1"), 6, 0),
            ("2", lambda: self.logic.append_digit("2"), 6, 1),
            ("3", lambda: self.logic.append_digit("3"), 6, 2),
            ("-", lambda: self.logic.set_operation("-"), 6, 3),
            ("%", self.logic.percent, 6, 4),
            ("0", lambda: self.logic.append_digit("0"), 7, 0),
            (".", self.logic.append_decimal, 7, 1),
            ("±", self.logic.negate, 7, 2),
            ("+", lambda: self.logic.set_operation("+"), 7, 3),
            ("=", self.logic.evaluate, 7, 4),
            ("^", lambda: self.logic.set_operation("^"), 8, 0),
            ("mod", lambda: self.logic.set_operation("mod"), 8, 1),
            ("!", self.logic.factorial, 8, 2),
            ("j", self.logic.append_complex, 8, 3),
            ("RAD/DEG", self.logic.toggle_angle_mode, 8, 4),
            ("m→cm", lambda: self.logic.convert_unit("m_to_cm"), 9, 0),
            ("cm→m", lambda: self.logic.convert_unit("cm_to_m"), 9, 1),
            ("kg→g", lambda: self.logic.convert_unit("kg_to_g"), 9, 2),
            ("g→kg", lambda: self.logic.convert_unit("g_to_kg"), 9, 3),
            ("C→F", lambda: self.logic.convert_unit("c_to_f"), 9, 4),
            ("F→C", lambda: self.logic.convert_unit("f_to_c"), 10, 0),
            ("km→m", lambda: self.logic.convert_unit("km_to_m"), 10, 1),
            ("m→km", lambda: self.logic.convert_unit("m_to_km"), 10, 2),
            ("c", lambda: self.logic.insert_constant("c"), 10, 3),
            ("g", lambda: self.logic.insert_constant("g"), 10, 4),
            ("Graph Sin", lambda: self.logic.graph_function("sin"), 11, 0),
            ("Graph Cos", lambda: self.logic.graph_function("cos"), 11, 1),
            ("Graph Tan", lambda: self.logic.graph_function("tan"), 11, 2),
            ("History", self.display.update_history, 11, 4)
        ]

        self.buttons = {}
        for text, command, row, col in button_layout:
            btn = ttk.Button(
                self.frame,
                text=text,
                command=lambda cmd=command: self.update_display(cmd),
                style="Calc.TButton"
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2)
            self.buttons[text] = btn

        ##Configure grid weights
        for i in range(12):
            self.frame.grid_rowconfigure(i, weight=1)
        for i in range(5):
            self.frame.grid_columnconfigure(i, weight=1)

    def update_display(self, command):
        """Handles button clicks and updates the display."""
        result = command()
        if command in [self.logic.evaluate, self.logic.clear, self.logic.clear_entry]:
            self.display.update_history()
        if command == self.logic.toggle_angle_mode:
            self.display.update_mode(result)
        else:
            self.display.update(result)
        self.display.update_memory(self.logic.memory)

    def update_theme(self, theme, colors):
        """Updates button theme (handled via ttk.Style in main.py)."""
        pass  ##Theme is applied globally via style configuration