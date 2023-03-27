def summ(list1):
    list2 = []
    for i in list1:
        list2.append(len(i))
    return list2

def start():
    list1 = ["hi hello","how","are yiu"]
    result = summ(list1)
    print(result)

start()