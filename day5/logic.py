from model import employees, EmployeeStatus
def get_employee_details(n):

    if employees.get(n) is not None:
        return EmployeeStatus(1, "Found", employees[n])
    else:
        return EmployeeStatus(0, "Not Found", None)

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
