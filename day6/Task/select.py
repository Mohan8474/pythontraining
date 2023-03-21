import sqlite3


def getDeveloperInfo():
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_select_query = """select * from Task """
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        # print("Printing ID ", id)

        found = False

        for row in records:
            found = True
            print("ID  = ", row[0])
            print("name  = ", row[1])
            print("priority  = ", row[2])


        if found == False:
            print("no ID found")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")


getDeveloperInfo()