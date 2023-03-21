from listlogic import listop
def start():
    n =int(input("Enter Number of elements to be added in list: "))
    list1 = []
    for i in range(n):
        list1.append(input("Enter String: "))
    a = int(input("Enter Number to Extract: "))
    result = listop(list1,a)
    print(result)

