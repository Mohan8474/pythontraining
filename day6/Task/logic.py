from taskdb import get_task_details, get_tasks_priority, update_task_details

def get_details(n):
    return get_task_details(n)


def get_details_id(priority):
    return get_tasks_priority(priority)

def update_details(id, name, priority):
    return update_task_details(id, name, priority)

