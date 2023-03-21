def lenc(str):
    a = len(str.split())
    return a

def count(str, str1):
    if str1 in str:
        return str.count(str1)
    else:
        return -1

def exit():
    return "End"

def countc():
    str = input("Enter a String: ")
    str1 = input("Enter String: ")
    result1 = count(str, str1)
    print( result1)

def lengthc():
    str = input("Enter String: ")
    result = lenc(str)
    print(result)

def start():
    print("1. To check Length\n2. For check count\n0. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        lengthc()
    elif ch == 2:
        countc()
    elif ch == 0:
        exit()
    else:
        print("Invalid Choice")

start()


