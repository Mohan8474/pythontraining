import random
from random import randint
list1 = []
def fill(a,b):
    list1.clear()
    for i in range(10):
        list1.append(random.randint(a,b))
    return list1
def view():
    return list1
def change(a,b):
    for i in range(len(list1)):
        if list1[i] == a:
            list1[i] = b
    return list1
def remove(a):
    list1.remove(a)
    return list1
def sorta(list1):
    a = sorted(list1)
    return a
def sortd(list1):
    a = sorted(list1, reverse=True)
    return a



