
from empdb import get_employee_details, get_employees_by_dept_id

def get_details(n):
    return get_employee_details(n)

def get_details_id(dept_id):
    return get_employees_by_dept_id(dept_id)


