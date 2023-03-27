def summ(list1):
    count = 0
    for i in list1:
        check = list1.count(i)
        if (check > count):
            count = check
            num = i

    return num

def start():
    list1 = [1,2,3,4,3,2,3,4,5]
    result = summ(list1)
    print(result)

start()