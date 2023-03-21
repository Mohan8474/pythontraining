from model import employees
def get_employee_details(emp_no):
    if emp_no in employees:
        return str(employees[emp_no])
    else:
        return "Employee not found"

def get_employees_by_dept_id(dept_id, employees):
    dept_employees = []
    for emp_no, emp in employees.items():
        if emp.dept_id == dept_id:
            dept_employees.append(str(emp))
    if dept_employees:
        return "\n".join(dept_employees)
    else:
        return "No employees found for the given department ID"

def viewall():
    return employees
