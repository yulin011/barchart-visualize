import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class BarchartVisualizationApp:
    def __init__(self, main_window):
        self.main_window = main_window
        self.main_window.title("Barchart Visualization")

        # Data upload area
        self.data_frame = ttk.Frame(self.main_window)
        self.data_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.upload_label = ttk.Label(self.data_frame, text="Data Upload ")
        self.upload_label.grid(row=0, column=0, pady=(0, 10))

        # Modify to a 5*5 data input area
        self.data_entry_widgets = []
        for i in range(5):
            for j in range(5):
                data_entry = ttk.Entry(self.data_frame, width=5)
                data_entry.grid(row=i+1, column=j, pady=3, padx=3)
                self.data_entry_widgets.append(data_entry)

        # Parameter selection area
        self.param_frame = ttk.Frame(self.main_window)
        self.param_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.param_label = ttk.Label(self.param_frame, text="Input area")
        self.param_label.grid(row=0, column=0, pady=(0, 10))

        self.title_label = ttk.Label(self.param_frame, text="Title:")
        self.title_label.grid(row=1, column=0, pady=(0, 5))
        self.title_entry = ttk.Entry(self.param_frame)
        self.title_entry.grid(row=1, column=1, pady=(0, 5))

        # show bar chart
        self.chart_type_label = ttk.Label(self.param_frame, text="Chart Type: Bar Chart")
        self.chart_type_label.grid(row=2, column=0, pady=(0, 5))

        self.preview_button = ttk.Button(self.param_frame, text="Generate Preview", command=self.generate_preview)
        self.preview_button.grid(row=3, column=0, columnspan=2, pady=(10, 0))


        # Preview
        self.preview_frame = ttk.Frame(self.main_window)
        self.preview_frame.pack(side=tk.TOP, padx=10, pady=10)

        self.preview_label = ttk.Label(self.preview_frame, text="Preview")
        self.preview_label.grid(row=0, column=0, pady=(0, 10))

        self.preview_canvas = tk.Canvas(self.preview_frame, width=400, height=300)
        self.preview_canvas.grid(row=1, column=0, pady=(0, 10))

    def get_data(self):
        data = []
        for entry in self.data_entry_widgets:
            value = entry.get()
            if not value:
                messagebox.showerror("Error", "Please fill in all data")
                return None
            try:
                data.append(float(value))
            except ValueError:
                messagebox.showerror("Error", "Data must be numeric")
                return None
        return data

    def generate_preview(self):
        data = self.get_data()
        title = self.title_entry.get()

        if not data or not title:
            messagebox.showerror("Error", "Please fill in all necessary parameters")
            return

        plt.figure(figsize=(4, 3), dpi=100)
        plt.title(title)
        plt.bar(range(1, 26), data)  # Modify to 25 data points

        self.show_preview()

    def show_preview(self):
        plt.tight_layout()
        self.preview_canvas.delete("all")
        self.preview_canvas.draw_idle()
        canvas_agg = FigureCanvasTkAgg(plt.gcf(), master=self.preview_canvas)
        canvas_agg.draw()
        canvas_agg.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvas_agg.get_tk_widget().config(borderwidth=0, highlightthickness=0)

if __name__ == "__main__":
    main_window = tk.Tk()
    app = BarchartVisualizationApp(main_window)
    main_window.mainloop()
