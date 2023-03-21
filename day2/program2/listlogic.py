def listop(list1,a):
    list2 = []
    for i in list1:
        list2.append(i.split("."))
    if a == 1:
        list3 = []
        for i in list2:
            list3.append(int(i[0]))
        return list3
    elif a == 2:
        list4 = []
        for i in list2:
            list4.append(i[1])
        return list4
    elif a == 3:
        list5 = []
        for i in list2:
            list5.append(int(i[2]))
        return list5



# A = ["1.3.4","4.5.6"]
# list1=[]
# list2=[]
# for i in A:
#     list1.append(i.split("."))
# for i in list1:
#     list2.append(int(i[0]))
# print(list2)
