import sqlite3
from model import Task

def updateSqliteTable(task):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sql_update_query = """Update task set priority = ?, name = ? where ID = ?"""
        data = (task.ID, task.name, task.priority )
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()
        print(cursor.rowcount)
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

task = Task(1, "orange", 12)
updateSqliteTable(task)