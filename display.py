import tkinter as tk
from tkinter import ttk

class CalculatorDisplay:
    def __init__(self, parent, logic):
        self.logic = logic
        self.frame = ttk.Frame(parent)
        self.frame.grid(row=0, column=0, columnspan=5, sticky="nsew", padx=5, pady=5)

        ##History display
        self.history_var = tk.StringVar(value="History")
        self.history_label = ttk.Label(
            self.frame,
            textvariable=self.history_var,
            font=("Arial", 10),
            anchor="w",
            wraplength=580
        )
        self.history_label.pack(fill="x", pady=2)

        ##Main display
        self.main_var = tk.StringVar(value="0")
        self.main_display = ttk.Label(
            self.frame,
            textvariable=self.main_var,
            font=("Arial", 28, "bold"),
            anchor="e",
            padding=10
        )
        self.main_display.pack(fill="both", expand=True)

        ##Indicators
        self.indicator_frame = ttk.Frame(self.frame)
        self.indicator_frame.pack(fill="x")
        self.memory_var = tk.StringVar(value="")
        self.mode_var = tk.StringVar(value="RAD")
        self.memory_label = ttk.Label(
            self.indicator_frame,
            textvariable=self.memory_var,
            font=("Arial", 12)
        )
        self.mode_label = ttk.Label(
            self.indicator_frame,
            textvariable=self.mode_var,
            font=("Arial", 12)
        )
        self.memory_label.pack(side="left", padx=5)
        self.mode_label.pack(side="right", padx=5)

    def update(self, value):
        self.main_var.set(value)

    def update_memory(self, value):
        self.memory_var.set("M" if value != 0 else "")

    def update_mode(self, mode):
        self.mode_var.set(mode)

    def update_history(self):
        self.history_var.set(self.logic.get_history())

    def update_theme(self, theme):
        if theme == "dark":
            self.main_display.configure(style="Dark.TLabel")
            self.history_label.configure(style="Dark.TLabel")
            self.memory_label.configure(style="Dark.TLabel")
            self.mode_label.configure(style="Dark.TLabel")
            self.style.configure("Dark.TLabel", background="#1e1e1e", foreground="white")
        elif theme == "light":
            self.main_display.configure(style="Light.TLabel")
            self.history_label.configure(style="Light.TLabel")
            self.memory_label.configure(style="Light.TLabel")
            self.mode_label.configure(style="Light.TLabel")
            self.style.configure("Light.TLabel", background="#f0f0f0", foreground="black")