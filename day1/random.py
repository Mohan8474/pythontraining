import random

def randomn(num1,num2):
    return random.randint(num1,num2)

def start():
    num1 = int(input("Enter a Starting Number: "))
    num2 = int(input("Enter a Ending Number: "))
    result = randomn(num1,num2)
    print(f"Random number between {num1} and {num2} is {result}")

start()