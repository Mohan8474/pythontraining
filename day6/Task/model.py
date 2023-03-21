class Task:
    def __init__(self, ID, name, priority):
        self.ID = ID
        self.name = name
        self.priority = priority

    def __repr__(self):
        return f"ID: {self.ID}, Name: {self.name}, Priority: {self.priority}"
