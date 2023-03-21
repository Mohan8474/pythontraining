from logic import get_employee_details, get_employees_by_dept_id, viewall
from model import employees


def pres():
    exit = False
    while not exit:
        print("1. View Specific\n2. Get employees by department ID\n3. View All Employees\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            n = int(input("Enter employee ID:"))
            res = get_employee_details(n)
            if res.status_code == 1:
                print(f"Status Code: {res.status_code}\nMessage: {res.message}\nEmployee Details: {res.employee_obj}")
            else:
                print(f"Status Code: {res.statusCode}\nMessage: {res.message}\nEmployee Details: {res.employee_obj}")
        elif choice == "2":
            dept_id = int(input("Enter department ID: "))
            print(get_employees_by_dept_id(dept_id, employees))
        elif choice == "3":
            result = viewall()
            print(result)
        elif choice == "0":
            exit == True
        else:
            print("Invalid choice. Please try again.")