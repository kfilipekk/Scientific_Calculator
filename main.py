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
        self.style.configure("TFrame", background="#1e1e1e")
        self.style.configure("TLabel", background="#1e1e1e", foreground="white")
        self.style.configure("Dark.TButton", background="#333333", foreground="white", borderwidth=0)
        self.style.configure("Light.TButton", background="#e0e0e0", foreground="black", borderwidth=0)

        self.logic = CalculatorLogic()
        self.display = CalculatorDisplay(self.root, self.logic)
        self.buttons = CalculatorButtons(self.root, self.display, self.logic)

        self.create_menu()

        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)

        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Dark", command=lambda: self.set_theme("dark"))
        theme_menu.add_command(label="Light", command=lambda: self.set_theme("light"))

        help_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.show_about)

    def set_theme(self, theme):
        if theme == "dark":
            self.root.configure(bg="#1e1e1e")
            self.style.configure("TFrame", background="#1e1e1e")
            self.style.configure("TLabel", background="#1e1e1e", foreground="white")
            self.display.update_theme("dark")
            self.buttons.update_theme("dark")
        elif theme == "light":
            self.root.configure(bg="#f0f0f0")
            self.style.configure("TFrame", background="#f0f0f0")
            self.style.configure("TLabel", background="#f0f0f0", foreground="black")
            self.display.update_theme("light")
            self.buttons.update_theme("light")

    def show_about(self):
        messagebox.showinfo("About", "Advanced Scientific Calculator\nVersion 1.0\nBuilt with Python and Tkinter")

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    app.run()
