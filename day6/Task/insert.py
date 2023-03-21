import sqlite3
from model import Task

def insertVaribleIntoTable(task):
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_query = """INSERT INTO task
                          (ID,name,priority) 
                           VALUES 
                          (?,?,?)"""

        data_tuple = (task.ID, task.name, task.priority)
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

task = Task(6, "Finish ", 8)
insertVaribleIntoTable(task)




#insertVaribleIntoTable(13, 'Ben', 6,7,8)