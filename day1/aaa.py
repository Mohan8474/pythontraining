
def maximumSum(list1):
    maxi = 0
    for x in list1:
        sum = 0
        for y in x:
            sum += y
        maxi = max(sum, maxi)

    return maxi

def start():
    list1 = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
    result = maximumSum(list1)
    print(result)

start()