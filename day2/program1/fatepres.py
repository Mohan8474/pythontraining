from fatelogic import fill, view, change, remove, list1, sorta, sortd

def start():
    exit = False
    while not exit:
        print("1. To Fill List\n2. To View List\n3. To Change Element in List"
              "\n4. To Remove Element in List\n5. Sort in Ascending Order\n6. Sort in Descending Order\n0. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            a = int(input("Enter Starting Number: "))
            b = int(input("Enter Ending Number: "))
            result = fill(a,b)
            print(result)
        elif ch == 2:
            result = view()
            print(result)
        elif ch == 3:
            a = int(input("Enter Number Which you want to replace it: "))
            while a not in list1:
                print(f"{a} is not in list enter another number")
                a = int(input("Enter Number Which you want to replace it: "))
            b = int(input("Enter Number Which should replace: "))
            while b in list1:
                print(f"{b} is already in list enter another number")
                b = int(input("Enter Number Which you want to replace it: "))
            result = change(a,b)
            print(result)
        elif ch == 4:
            a = int(input("Enter Number Which you want to remove : "))
            while a not in list1:
                print(f"{a} is not in list enter another number")
                a = int(input("Enter Number Which you want to remove: "))
            result = remove(a)
            print(result)
        elif ch == 5:
            result = sorta(list1)
            print(result)
        elif ch == 6:
            result = sortd(list1)
            print(result)
        elif ch == 0:
            exit = True
        else:
            print("Invalid Choice")

# def start():
#     exit = False
#     while not exit:
#         print("1. To Fill List\n2. To View List\n3. To Change Element in List\n4. To Remove Element in List\n0. Exit")
#         ch = int(input("Enter your choice: "))
#         if ch == 1:
#             fill()
#         elif ch == 2:
#             view()
#         elif ch == 3:
#             change()
#         elif ch == 4:
#             remove()
#         elif ch == 0:
#             exit = True
#         else:
#             print("Invalid Choice")

# def fill1(a,b):
#     a = int(input("Enter Starting Number: "))
#     b = int(input("Enter Ending Number: "))
#     result = fill(a, b)
#     print(result)




