from tkinter import *
import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

class UserTotalView:
    def __init__(self, total_amount):
        win = Tk()
        win.title("Total Pay")
        win.geometry("300x200")
        win.configure(background='azure2')
        win.resizable(width=False, height=False)

        def upload_image():
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
            if file_path:
                image = Image.open(file_path)
                image.thumbnail((200, 200))
                photo = ImageTk.PhotoImage(image)
                image_label.config(image=photo)
                image_label.image = photo


        upload_button = tk.Button(win, text="Upload payment image", bg="black", fg="white",
                                  font=("Arial", "11"), command=upload_image)
        upload_button.place(x=70, y=120)

        image_label = tk.Label(win, background='azure2')
        image_label.pack(side=tk.BOTTOM)

        Label(win, text="Please pay the amount to this card number",
              background="azure2", font=("Helvetica", "9")).place(x=30, y=10)
        Label(win, text="6219 8619 9984 3005", bg='azure2', font=("Helvetica", "12"),
              borderwidth=1, relief="solid", border="3").place(x=70, y=80)

        Label(win, text="Total amount:", background="azure2", font=("Helvetica", "11")).place(x=20, y=30)
        total_entry = tk.Entry(win, font=("Helvetica", "11"), width=15, justify="center", state="readonly")
        total_entry.place(x=150, y=30)


        total_entry.config(state="normal")
        total_entry.delete(0, END)
        total_entry.insert(0, str(total_amount))
        total_entry.config(state="readonly")

        win.mainloop()
