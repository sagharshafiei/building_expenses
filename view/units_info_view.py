from controller.units_info_controller import *
from view.component import *


class UnitsInfoView:
    # Refresh Button Function
    def reset_form(self):
        self.id.variable.set(0)
        self.unit_no.variable.set(0)
        self.first_name.variable.set("")
        self.family_name.variable.set("")
        self.resident_count.variable.set(0)
        status, data_list = find_all()
        sorted_data_list = sorted(data_list, key=lambda x: x.unit_no)
        self.table.refresh_table(sorted_data_list)

    # Save Button Function
    def save_click(self):
        status, data = save(self.unit_no.variable.get(),
                            self.first_name.variable.get(),
                            self.family_name.variable.get(),
                            self.resident_count.variable.get()
                            )
        if status:
            msg.showinfo("Save", f"Unit Saved\n{data}")
            self.reset_form()
        else:
            msg.showerror("Save Error", f"Error\n{data}")

    # Edit Button Function
    def edit_click(self):
        status, data = edit(self.id.variable.get(),
                            self.unit_no.variable.get(),
                            self.first_name.variable.get(),
                            self.family_name.variable.get(),
                            self.resident_count.variable.get()
                            )
        if status:
            msg.showinfo("Edit", f"Unit Edited\n{data}")
            self.reset_form()
        else:
            msg.showerror("Edit Error", f"Error\n{data}")

    # Remove Button Function
    def remove_click(self):
        status, data = remove_by_id(self.id.variable.get())
        if status:
            msg.showinfo("Remove", f"Unit Removed\n{data}")
            self.reset_form()
        else:
            msg.showerror("Remove Error", f"Error\n{data}")

    def select_table(self, selected_item):
        self.id.variable.set(selected_item[0])
        self.unit_no.variable.set(selected_item[1])
        self.first_name.variable.set(selected_item[2])
        self.family_name.variable.set(selected_item[3])
        self.resident_count.variable.set(selected_item[4])

    def __init__(self):
        self.win = Toplevel()
        self.win.title("User Info Panel")
        self.win.geometry("595x500")
        self.win.configure(background='azure2')
        self.win.resizable(width=False, height=False)


        self.id = LabelAndEntry(self.win, "Id", 20, 20, distance=110, state="readonly")
        self.unit_no = LabelAndEntry(self.win, "Unit No:", 310, 20, distance=110)
        self.first_name = LabelAndEntry(self.win, "First Name:", 20, 60, distance=110)
        self.family_name = LabelAndEntry(self.win, "Family Name:", 310, 60, distance=110)
        self.resident_count = LabelAndEntry(self.win, "Resident Count:", 20, 105, distance=110)

        self.table = Table(
            self.win,
            ["Id", "Unit No.", "First Name", "Family Name", "Resident Count"],
            [60, 60, 130, 130, 130],
            290,
            40, 140,
            self.select_table,
        )

        TkButton(self.win, "Save", self.save_click, 80, 445)
        TkButton(self.win, "Edit", self.edit_click, 190, 445)
        TkButton(self.win, "Remove", self.remove_click, 300, 445)
        TkButton(self.win, "Refresh", self.reset_form, 410, 445)

        self.reset_form()


        self.win.mainloop()

# a=UnitsInfoView()