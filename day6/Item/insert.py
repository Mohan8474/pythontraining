import sqlite3

def insertVaribleIntoTable(id, name, price, category):
    try:
        sqliteConnection = sqlite3.connect('item.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO Item
                          (itemno,name,price,category) 
                           VALUES 
                          (?,?,?,?)"""

        data_tuple = (id, name, price, category)
        cursor.execute(sqlite_insert_query, data_tuple)
        #print(cursor.rowcount)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into SqliteDb_developers table")

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The SQLite connection is closed")

insertVaribleIntoTable(1, "Book", 30, "Stationary")
insertVaribleIntoTable(2, "Pen", 10, "Stationary")
insertVaribleIntoTable(3, "Apple", 120, "Food")
insertVaribleIntoTable(4, "Maaza", 35, "Drinks")

#insertVaribleIntoTable(13, 'Ben', 6,7,8)