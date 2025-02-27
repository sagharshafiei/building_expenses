from model.da.da import DataAccess
from model.entity import Expenses, Units

# from model.tools.logging import Logger

def find_all():
    try:
        expense_da = DataAccess(Expenses)
        expense_list = expense_da.find_all()
        # Logger.info(f"expense FindALL")
        return True, expense_list
    except Exception as e:
        # Logger.error(f"{e} - FindALL")
        return False, f"{e}"

def sum_residents():
    people_counter = []
    units_da = DataAccess(Units)
    people_count_list = units_da.find_by(Units._no_people)

    for item in people_count_list:
        people_counter.append(item.no_people)
    else:
        return sum(people_counter)


def expense_calculator(resident_count):
    status, expense_list = find_all()

    for item in expense_list:
        item.water = int((item.water / sum_residents()) * resident_count)
        item.electricity = int((item.electricity / sum_residents()) * resident_count)
        item.gas = int((item.gas / sum_residents()) * resident_count)
        item.elevator = int((item.elevator / sum_residents()) * resident_count)
        item.cleaning = int((item.cleaning / sum_residents()) * resident_count)
        item.engine_room = int((item.engine_room / sum_residents()) * resident_count)
        item.other = int((item.other / sum_residents()) * resident_count)
        item.total = int((item.total / sum_residents()) * resident_count)
    return expense_list


