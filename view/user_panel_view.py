from tkinter import Tk, Label, Button
from model.entity import UnitUserConnector, Users, Units
from view.component import LabelAndEntry, Table
from model.da.da import DataAccess
from controller.user_panel_controller import expense_calculator
from view.user_total_view import UserTotalView


class UserPanelView:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.win = Tk()
        self.win.title("User Panel")
        self.win.geometry("790x500")
        self.win.configure(background='azure2')
        self.win.resizable(False, False)

        user_da = DataAccess(Users)
        user = user_da.find_by((Users._username == self.username) & (Users._password == self.password))
        user_id = user[0].id

        connector_da = DataAccess(UnitUserConnector)
        unit_user_item = connector_da.find_by(UnitUserConnector.user_id == user_id)
        unit_id = unit_user_item[0].unit_id

        unit_da = DataAccess(Units)
        unit = unit_da.find_by_id(unit_id)
        self.unit_no = unit.unit_no
        self.first_name = unit.name
        self.family_name = unit.family
        self.resident_count = unit.no_people

        Label(self.win, text=f"Welcome {self.first_name} {self.family_name}!",
              font=("Arial", "18"), foreground="green", background='azure2', border="15").place(x=230, y=15)

        LabelAndEntry(self.win, "Unit Number:", 80, 100, 100, state="readonly").variable.set(self.unit_no)
        LabelAndEntry(self.win, "Residents Count:", 450, 100, 120, state="readonly").variable.set(self.resident_count)

        Button(self.win, text="show total amount", font=("Arial", "13"),
               command=self.total_show).place(x=320, y=440)

        self.table = Table(self.win,
                           ["Id", "month", "water", "electricity", "gas", "elevator", "cleaning", "engine_room",
                            "other", "total"],
                           [40, 80, 80, 80, 80, 80, 80, 80, 80, 80],
                           300, 15, 130)

        self.read_data()

        self.win.mainloop()

    def read_data(self):
        result_list = expense_calculator(self.resident_count)
        self.total_data = result_list
        self.table.refresh_table(result_list)

    def total_show(self):
        if hasattr(self, 'total_data') and self.total_data:
            last_total = self.total_data[-1].total
        else:
            last_total = 0

        UserTotalView(total_amount=last_total)

# a = UserPanelView("username1", "password1")
