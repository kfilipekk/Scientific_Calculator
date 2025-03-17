import tkinter as tk
from tkinter import ttk, messagebox, colorchooser
from calculator import CalculatorLogic
from buttons import CalculatorButtons
from display import CalculatorDisplay
from graphing import GraphingFrame
import json
import os

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("600x800")
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e1e")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.logic = CalculatorLogic()
        self.display = CalculatorDisplay(self.root, self.logic)
        self.buttons = CalculatorButtons(self.root, self.display, self.logic)

        ##Define default themes
        self.themes = {
            "dark": {"bg": "#1e1e1e", "fg": "white", "button_bg": "#333333", "button_fg": "white"},
            "light": {"bg": "#f0f0f0", "fg": "black", "button_bg": "#e0e0e0", "button_fg": "black"},
            "blue": {"bg": "#0a2b4e", "fg": "white", "button_bg": "#1a3a5e", "button_fg": "white"},
            "green": {"bg": "#1e3e1e", "fg": "white", "button_bg": "#2e4e2e", "button_fg": "white"},
        }
        self.current_theme = "dark"
        self.custom_theme = self.load_custom_theme()
        self.set_theme(self.current_theme)

        self.create_menu()
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_menu(self):
        """Creates the menu bar with theme and graph options."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        ##Theme menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        for theme_name in self.themes.keys():
            theme_menu.add_command(
                label=theme_name.capitalize(),
                command=lambda t=theme_name: self.set_theme(t)
            )
        theme_menu.add_command(label="Custom", command=self.open_custom_theme_dialog)

        ##Graph menu
        graph_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Graph", menu=graph_menu)
        graph_menu.add_command(label="Plot Function", command=self.open_graphing_interface)

        ##Help menu
        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def set_theme(self, theme):
        """Sets the selected theme and updates the UI."""
        self.current_theme = theme
        if theme == "custom":
            colors = self.custom_theme
        else:
            colors = self.themes[theme]
        self.apply_theme(colors)

    def apply_theme(self, colors):
        """Applies the theme colours to all components."""
        self.root.configure(bg=colors["bg"])
        self.style.configure("TFrame", background=colors["bg"])
        self.style.configure("TLabel", background=colors["bg"], foreground=colors["fg"])
        self.style.configure("Calc.TButton", background=colors["button_bg"], foreground=colors["button_fg"])
        self.display.update_theme(colors)
        self.buttons.update_theme(colors)

    def open_custom_theme_dialog(self):
        """Opens a dialog for users to select custom theme colours."""
        dialog = tk.Toplevel(self.root)
        dialog.title("Custom Theme")
        dialog.geometry("300x200")

        ##Colour selection labels and buttons
        labels = ["Background", "Button Background", "Text Colour"]
        color_keys = ["bg", "button_bg", "fg"]
        for i, label in enumerate(labels):
            tk.Label(dialog, text=label).grid(row=i, column=0, padx=5, pady=5)
            color_button = tk.Button(
                dialog,
                text="Choose Colour",
                command=lambda key=color_keys[i]: self.choose_color(key)
            )
            color_button.grid(row=i, column=1, padx=5, pady=5)

        apply_button = tk.Button(dialog, text="Apply", command=lambda: self.set_theme("custom"))
        apply_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

    def choose_color(self, key):
        """Opens a colour chooser and updates the custom theme."""
        color = colorchooser.askcolor()[1]
        if color:
            self.custom_theme[key] = color
            self.save_custom_theme()

    def save_custom_theme(self):
        """Saves the custom theme to a JSON file."""
        with open("custom_theme.json", "w") as f:
            json.dump(self.custom_theme, f)

    def load_custom_theme(self):
        """Loads the custom theme from a JSON file."""
        if os.path.exists("custom_theme.json"):
            with open("custom_theme.json", "r") as f:
                return json.load(f)
        return {"bg": "#1e1e1e", "fg": "white", "button_bg": "#333333", "button_fg": "white"}

    def open_graphing_interface(self):
        """Opens the graphing interface in a new window."""
        graph_window = tk.Toplevel(self.root)
        graph_window.title("Graph Function")
        graph_window.geometry("600x600")
        graph_frame = GraphingFrame(graph_window, self.logic, self.current_theme, self.themes)
        graph_frame.pack(fill="both", expand=True)

    def show_about(self):
        """Displays the about dialog."""
        messagebox.showinfo("About", "Advanced Scientific Calculator\nVersion 1.0\nBuilt with Python and Tkinter")

    def run(self):
        """Runs the application."""
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()