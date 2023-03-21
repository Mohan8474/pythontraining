import sqlite3
from model import Employee, EmployeeStatus

def get_employee_details(n):
    es = EmployeeStatus(0, "Not Found", None)
    try:
        sqliteConnection = sqlite3.connect('emp.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from emp where ID = ?"""
        cursor.execute(sql_select_query,(n,))
        records = cursor.fetchall()
        # print("Printing ID ", id)
        for row in records:
            e = Employee(row[0], row[1], row[2])
            es.status_code = 1
            es.message = "Found"
            es.employee_obj = e

        cursor.close()

    except sqlite3.Error as error:
        # print("Failed to read data from sqlite table", error)
        es.message = error
    finally:
        if sqliteConnection:
            sqliteConnection.close()
    return es

def get_employees_by_dept_id(dept_id):
    el = []
    try:
        sqliteConnection = sqlite3.connect('emp.db')
        cursor = sqliteConnection.cursor()

        sql_select_query = """select * from emp where dept_id = ?"""
        cursor.execute(sql_select_query,(dept_id,))
        records = cursor.fetchall()
        for row in records:
            e = Employee(row[0], row[1], row[2])
            el.append(e)

        cursor.close()

    except sqlite3.Error as error:
        print("Failed to read data from sqlite table", error)
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
