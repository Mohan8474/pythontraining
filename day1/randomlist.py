import random

def randomn(num1,num2):
    i = 10
    list1 = []
    for i in range(10):
        list1.append(random.randint(10,20))
    return list1


def start():
    result = randomn(10,20)
    print(f"Random number list between 10 and 20 is {result}")

start()