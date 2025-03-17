##main.py
import tkinter as tk
from tkinter import ttk, messagebox
from calculator import CalculatorLogic
from buttons import CalculatorButtons
from display import CalculatorDisplay

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Scientific Calculator")
        self.root.geometry("600x800")
        self.root.resizable(True, True)
        self.root.configure(bg="#1e1e1e")

        self.style = ttk.Style()
        self.style.theme_use("clam")

        ##Initialise components
        self.logic = CalculatorLogic()
        self.display = CalculatorDisplay(self.root, self.logic)
        self.buttons = CalculatorButtons(self.root, self.display, self.logic)

        ##Define themes with colour configurations
        self.themes = {
            "dark": {"bg": "#1e1e1e", "fg": "white", "button_bg": "#333333", "button_fg": "white"},
            "light": {"bg": "#f0f0f0", "fg": "black", "button_bg": "#e0e0e0", "button_fg": "black"},
            "blue": {"bg": "#0a2b4e", "fg": "white", "button_bg": "#1a3a5e", "button_fg": "white"},
            "green": {"bg": "#1e3e1e", "fg": "white", "button_bg": "#2e4e2e", "button_fg": "white"},
        }
        self.current_theme = "dark"
        self.apply_theme(self.current_theme)

        self.create_menu()

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_menu(self):
        """Creates the menu bar with theme options."""
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        for theme_name in self.themes.keys():
            theme_menu.add_command(
                label=theme_name.capitalize(),
                command=lambda t=theme_name: self.set_theme(t)
            )

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def set_theme(self, theme):
        """Sets the selected theme and updates the UI."""
        self.current_theme = theme
        self.apply_theme(theme)

    def apply_theme(self, theme):
        """Applies the theme colors to all components."""
        colors = self.themes[theme]
        self.root.configure(bg=colors["bg"])
        self.style.configure("TFrame", background=colors["bg"])
        self.style.configure("TLabel", background=colors["bg"], foreground=colors["fg"])
        self.style.configure("Calc.TButton", background=colors["button_bg"], foreground=colors["button_fg"])
        self.display.update_theme(theme, colors)
        self.buttons.update_theme(theme, colors)

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