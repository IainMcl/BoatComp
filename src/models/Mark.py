from uuid import uuid4


class Mark():
    def __init__(self, position, type):
        self.id = uuid4()
        self.position = position
        self.type = type
