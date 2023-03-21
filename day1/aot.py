def aot(a,b,c):
    s = (a + b + c) / 2
    return (s*(s-a)*(s-b)*(s-c)) ** 0.5

def start():
    a = int(input("Enter Side 1: "))
    b = int(input("Enter Side 2: "))
    c = int(input("Enter Side 3: "))
    result = aot(a,b,c)
    print("Area of Triangle: ",result)

start()