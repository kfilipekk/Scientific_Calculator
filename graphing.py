import tkinter as tk
from tkinter import messagebox, filedialog, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class GraphingFrame(tk.Frame):
    def __init__(self, parent, logic, theme, themes):
        super().__init__(parent)
        self.logic = logic
        self.theme = theme
        self.themes = themes
        self.colors = themes[theme]
        self.configure(bg=self.colors["bg"])

        self.color_options = ["blue", "red", "green", "orange", "purple", "black"]

        ## Function 1
        tk.Label(self, text="Function 1:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=0, column=0, padx=5, pady=5)
        self.func1_entry = tk.Entry(self, width=30)
        self.func1_entry.grid(row=0, column=1, padx=5, pady=5)
        self.color1_var = tk.StringVar(value="blue")
        ttk.Combobox(self, textvariable=self.color1_var, values=self.color_options).grid(row=0, column=2, padx=5, pady=5)

        ## Function 2
        tk.Label(self, text="Function 2:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=1, column=0, padx=5, pady=5)
        self.func2_entry = tk.Entry(self, width=30)
        self.func2_entry.grid(row=1, column=1, padx=5, pady=5)
        self.color2_var = tk.StringVar(value="red")
        ttk.Combobox(self, textvariable=self.color2_var, values=self.color_options).grid(row=1, column=2, padx=5, pady=5)

        ## X-range entries
        tk.Label(self, text="X-min:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=2, column=0, padx=5, pady=5)
        self.xmin_entry = tk.Entry(self, width=10)
        self.xmin_entry.insert(0, "-10")
        self.xmin_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self, text="X-max:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=3, column=0, padx=5, pady=5)
        self.xmax_entry = tk.Entry(self, width=10)
        self.xmax_entry.insert(0, "10")
        self.xmax_entry.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self, text="Points:", bg=self.colors["bg"], fg=self.colors["fg"]).grid(row=4, column=0, padx=5, pady=5)
        self.points_entry = tk.Entry(self, width=10)
        self.points_entry.insert(0, "400")
        self.points_entry.grid(row=4, column=1, padx=5, pady=5)

        ## Buttons
        plot_button = tk.Button(self, text="Plot", command=self.plot_function, bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        plot_button.grid(row=5, column=0, pady=10)

        clear_button = tk.Button(self, text="Clear", command=self.clear_plot, bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        clear_button.grid(row=5, column=1, pady=10)

        save_button = tk.Button(self, text="Save Plot", command=self.save_plot, bg=self.colors["button_bg"], fg=self.colors["button_fg"])
        save_button.grid(row=5, column=2, pady=10)

        ## Matplotlib figure
        self.fig, self.ax = plt.subplots(figsize=(5, 4))
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().grid(row=6, column=0, columnspan=3, padx=5, pady=5)

    def plot_function(self):
        """Plots the user-defined functions."""
        try:
            x_min = float(self.xmin_entry.get())
            x_max = float(self.xmax_entry.get())
            num_points = int(self.points_entry.get())
            self.ax.clear()

            functions = [
                (self.func1_entry.get(), self.color1_var.get()),
                (self.func2_entry.get(), self.color2_var.get())
            ]

            plotted = False
            for func_str, color in functions:
                if func_str.strip():
                    x_values, y_values = self.logic.graph_function(func_str, x_min, x_max, num_points)
                    self.ax.plot(x_values, y_values, label=func_str, color=color)
                    plotted = True

            if plotted:
                self.ax.set_title("Graph of Functions")
                self.ax.set_xlabel("x")
                self.ax.set_ylabel("y")
                self.ax.legend()
                self.canvas.draw()
            else:
                messagebox.showinfo("Info", "Please enter at least one function to plot.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def clear_plot(self):
        """Clears the plot."""
        self.ax.clear()
        self.canvas.draw()

    def save_plot(self):
        """Saves the current plot to a file."""
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
            if file_path:
                self.fig.savefig(file_path)
                messagebox.showinfo("Success", "Plot saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save plot: {e}")