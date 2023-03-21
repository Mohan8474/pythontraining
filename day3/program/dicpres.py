from dictlogic import addw, vieww, wordscount, wordsandcount
def start():
    exit = False
    while not exit:
        print("1. Add a Word\n2. View all Words\n3. View count of words"
              "\n4. view words with count\n0. Exit")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            key = input(("Enter word: "))
            addw(key)
            print("Word added Successfully")

        elif ch == 2:
            result = vieww()
            print(result)

        elif ch == 3:
            word = input("Enter word")
            count= wordscount(word)
            print(count)
        elif ch == 4:
            count = int(input("Enter the count to filter by: "))
            result =wordsandcount(count)
            print(result)
        elif ch == 0:
            exit = True
        else:
            print("Invalid Choice")

