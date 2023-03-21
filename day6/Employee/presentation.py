from logic import get_details, get_details_id
from model import Employee, EmployeeStatus


def pres():
    exit = False
    while not exit:
        print("1. View Specific By ID\n2. Get employees by department ID\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            n = int(input("Enter employee ID:"))
            res = get_details(n)
            if res.status_code == 0:
                print("No Employee Found")
            else:
                print(f"Status Code: {res.status_code}\nMessage: {res.message}\nEmployee Details: {res.employee_obj}")
        elif choice == "2":
            dept_id = int(input("Enter department ID: "))
            emp_list = get_details_id(dept_id)
            if len(emp_list) == 0:
                print("No Employees Found")
            else:
                for emp in emp_list:
                    print(emp)
        elif choice == "0":
            exit == True
        else:
            print("Invalid choice. Please try again.")