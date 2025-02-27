from model.da.da import DataAccess
from model.entity import Units


def save(unit_no, first, family, resident_count):
    try:
        unit_da = DataAccess(Units)
        unit = Units(unit_no, first, family, resident_count)

        unit_da.save(unit)
        return True, unit

    except Exception as e:
        return False, f"{e}"


def edit(id, unit_no, first, family, resident_count):
    try:
        unit = Units(unit_no, first, family, resident_count)
        unit.id = id
        unit_da = DataAccess(Units)

        unit_da.edit(unit)
        return True, unit

    except Exception as e:
        return False, f"{e}"


def remove_by_id(id):
    try:
        unit_da = DataAccess(Units)
        unit = unit_da.remove_by_id(id)
        return True, unit

    except Exception as e:
        return False, f"{e}"



def find_all():
    try:
        unit_da = DataAccess(Units)
        unit_list = unit_da.find_all()
        return True, unit_list

    except Exception as e:
        return False, f"{e}"