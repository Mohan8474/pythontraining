from logic import get_details, get_details_id, update_details
from model import Task


def pres():
    exit = False
    while not exit:
        print("1. View Specific By ID\n2. Get Tasks By priority\n3. Update Task\n0. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            n = int(input("Enter employee ID:"))
            res = get_details(n)
            print(res)
        elif choice == "2":
            priority = int(input("Enter priority: "))
            task_list = get_details_id(priority)
            if len(task_list) == 0:
                print("No Employees Found")
            else:
                for emp in task_list:
                    print(emp)
        elif choice == "3":
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            priority = int(input("Enter Priority: "))
            res = update_details(id, name, priority)
            print(res)
        elif choice == "0":
            exit == True
        else:
            print("Invalid choice. Please try again.")