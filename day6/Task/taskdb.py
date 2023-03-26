import sqlite3
from model import Task

def get_task_details(n):
    es = Task("Not Found", "Not Found", "Not Found")
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from task where ID = ?"""
        cursor.execute(sql_select_query,(n,))
        records = cursor.fetchall()
        # print("Printing ID ", id)
        for row in records:
            e = Task(row[0], row[1], row[2])
            es.ID = row[0]
            es.name = row[1]
            es.priority = row[2]

        cursor.close()

    except sqlite3.Error as error:
        # print("Failed to read data from sqlite table", error)
        es.message = error
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es

def get_tasks_priority(priority):
    el = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from task where priority = ?"""
        cursor.execute(sql_select_query,(priority,))
        records = cursor.fetchall()
        for row in records:
            e = Task(row[0], row[1], row[2])
            el.append(e)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return el


def update_task_details(id, name, priority):
    el = []
    try:
        sqliteConnection = sqlite3.connect('task.db')
        cursor = sqliteConnection.cursor()

        sql_update_query = """UPDATE task SET priority=?, name=? WHERE ID=?"""
        data = (priority, name, id)
        cursor.execute(sql_update_query, data)
        sqliteConnection.commit()

        sql_select_query = """SELECT * FROM task WHERE ID=?"""
        cursor.execute(sql_select_query, (id,))
        records = cursor.fetchall()
        for row in records:
            e = Task(row[0], row[1], row[2])
            el.append(e)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to update data in sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()

    return el

    # dept_employees = []
    # for emp_no, emp in employees.items():
    #     if emp.dept_id == dept_id:
    #         dept_employees.append(str(emp))
    # if dept_employees:
    #     return "\n".join(dept_employees)
    # else:
    #     return "No employees found for the given department ID"
