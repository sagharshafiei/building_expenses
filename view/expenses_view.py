from tkinter import *
from view.component import LabelAndEntry, Table,TkButton
import tkinter.messagebox as msg
from controller.expenses_controller import *

class ExpensesView:
    def select_table(self, selected_expense):
        self._id.variable.set(selected_expense[0])
        self._month.variable.set(selected_expense[1])
        self._water.variable.set(selected_expense[2])
        self._electricity.variable.set(selected_expense[3])
        self._gas.variable.set(selected_expense[4])
        self._elevator.variable.set(selected_expense[5])
        self._cleaning.variable.set(selected_expense[6])
        self._engine_room.variable.set(selected_expense[7])
        self._other.variable.set(selected_expense[8])

    # save
    def save_click(self):
        status, data = save(
            self._month.variable.get(),
            self._water.variable.get(),
            self._electricity.variable.get(),
            self._gas.variable.get(),
            self._elevator.variable.get(),
            self._cleaning.variable.get(),
            self._engine_room.variable.get(),
            self._other.variable.get(),
        )
        if status:
            msg.showinfo("Save", f"Expenses Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    # edit
    def edit_click(self):
        status, data = edit(
            self._id.variable.get(),
            self._month.variable.get(),
            self._water.variable.get(),
            self._electricity.variable.get(),
            self._gas.variable.get(),
            self._elevator.variable.get(),
            self._cleaning.variable.get(),
            self._engine_room.variable.get(),
            self._other.variable.get(),
        )
        if status:
            msg.showinfo("Edit", f"Expenses Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    # remove func
    def remove_click(self):
        status, data = remove_by_id(
            self._id.variable.get(),
        )
        if status:
            msg.showinfo("Remove", f"Expenses Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    # reset form
    def reset_form(self):
        self._id.variable.set(0)
        self._month.variable.set("")
        self._water.variable.set(0)
        self._electricity.variable.set(0)
        self._gas.variable.set(0)
        self._elevator.variable.set(0)
        self._cleaning.variable.set(0)
        self._engine_room.variable.set(0)
        self._other.variable.set(0)
        status, expense_list = find_all()
        self.table.refresh_table(expense_list)


    def __init__(self):
        self.win = Toplevel()
        self.win.title("Expenses")
        self.win.geometry("1250x470")
        self.win.configure(background='azure2')
        self.win.resizable(width=False, height=False)

        self._id = LabelAndEntry(self.win, "Id", 20, 20,100, data_type="int", state="readonly")
        self._month = LabelAndEntry(self.win, "Month:", 23, 70,100)
        self._water = LabelAndEntry(self.win, "water:", 23, 120,100)
        self._electricity = LabelAndEntry(self.win, "electricity:", 23, 170,100)
        self._gas = LabelAndEntry(self.win, "gas:", 23, 220,100)
        self._elevator = LabelAndEntry(self.win, "elevator:", 23, 270,100)
        self._cleaning = LabelAndEntry(self.win, "cleaning:", 23, 320,100)
        self._engine_room = LabelAndEntry(self.win, "engine room:", 23, 370,100)
        self._other = LabelAndEntry(self.win, "other:", 23, 420,100)

        self.table = Table(
            self.win,
            ["Id","month", "water", "electricity", "gas", "elevator", "cleaning", "engine_room",
             "other", "total"],
            [60, 100, 100, 100, 100, 100, 100, 100, 100, 100],
            350, 270, 20,
            self.select_table
        )

        TkButton(self.win,"Refresh",self.reset_form,450,390,130,50)
        TkButton(self.win,"Save",self.save_click,600,390,130,50)
        TkButton(self.win,"Edit",self.edit_click,750,390,130,50)
        TkButton(self.win,"Remove",self.remove_click,900,390,130,50)

        self.reset_form()


        self.win.mainloop()


# a = ExpensesView()