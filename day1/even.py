def evenorodd(num):
    if num%2 == 0:
        return "Even Number"
    else:
        return "Odd Number"

def start():
    num = int(input("Enter a Number: "))
    result = evenorodd(num)
    print(f"{num} is {result}")

start()