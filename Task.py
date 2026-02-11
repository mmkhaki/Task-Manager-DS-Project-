class Task:
    def __init__(self, id, st, et, value):
        self.id = id
        self.st = st
        self.et = et
        self.value = value
    
    def __str__(self):
        return f"Task => id:{self.id} |start time: {self.st} |end time: {self.et} |value: {self.value}"

    def __repr__(self):
        return self.__str__()