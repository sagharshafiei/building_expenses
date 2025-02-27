import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Combo Box Example")
win.geometry("300x200")

label = tk.Label(win, text="Select an option:")
label.pack(pady=10)

options = ["unit 1", "unit 2", "unit 3", "unit 4", "unit 5", "unit 6"]

combo = ttk.Combobox(win, values=options)
combo.pack(pady=10)


combo.current(0)
def get_value():
    selected_value = combo.get()
    label_result.config(text=f"Selected: {selected_value}")


btn = tk.Button(win, text="Get unit info", width=12, height=2, command=get_value)
btn.pack(pady=10)

label_result = tk.Label(win, text="Selected: None")
label_result.pack(pady=10)

win.mainloop()
