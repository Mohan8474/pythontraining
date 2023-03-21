class Employee:
    def __init__(self, ID, name, dept_id):
        self.ID = ID
        self.name = name
        self.dept_id = dept_id

    def __repr__(self):
        return f"Employee No: {self.ID}, Name: {self.name}, Dept ID: {self.dept_id}"

class EmployeeStatus:
    def __init__(self, status_code, message, employee_obj):
        self.status_code = status_code
        self.message = message
        self.employee_obj = employee_obj

    def __repr__(self):
        return f"Status Code: {self.status_code}, Message: {self.message}, Employee: {self.employee_obj}"
