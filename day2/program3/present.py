from logic import prevnum
def init():
    n = int(input("Enter a Number: "))
    result = prevnum(n)
    print(f"Previous Number is {result}")