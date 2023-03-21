from logic import get_employee_details, get_employees_by_dept_id, viewall
from model import employees


def pres():
    exit = False
    while not exit:
        print("1. View Specific\n2. Get employees by department ID\n3. View All Employees\n4. Status\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            emp_no = int(input("Enter employee number: "))
            print(get_employee_details(emp_no))
        elif choice == "2":
            dept_id = int(input("Enter department ID: "))
            print(get_employees_by_dept_id(dept_id, employees))
        elif choice == "3":
            result = viewall()
            print(result)
        elif choice == "4":
            pass
        elif choice == "0":
            exit == True
        else:
            print("Invalid choice. Please try again.")