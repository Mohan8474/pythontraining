import sqlite3

def updateSqliteTable(id, price, name):
    try:
        sqliteConnection = sqlite3.connect('item.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update Item set price = ?, name = ? where itemno = ?"""
        data = (price, name,  id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        if cursor.rowcount != 0:
            print("update successful")
        else:
            print("no rows where found in the table matching the where condition")


        print("Record Updated successfully")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("The sqlite connection is closed")

updateSqliteTable(1, 300, "mango")