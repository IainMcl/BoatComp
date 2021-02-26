from database.Table import Table


class Boat(Table):
    def __init__(self, name, **kwargs):
        self.name = name
