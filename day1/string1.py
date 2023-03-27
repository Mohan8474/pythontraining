def lenc(str):
    a = len(str.split())
    return a

def count(str, str1):
    if str1 in str:
        return str.count(str1)
    else:
        return -1

def start():
    str = input("Enter a String: ")
    str1 = input("Enter String: ")
    result = lenc(str)
    result1 = count(str, str1)
    print(f"No of words in the string are {result}")
    print( result1)


start()