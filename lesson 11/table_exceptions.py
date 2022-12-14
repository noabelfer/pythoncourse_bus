class TableExceptions(Exception):
    pass
class Tablesmall(TableExceptions):
    def __init__(self):
        super().__init__("table too small")

class Tableocc(TableExceptions):
    def __init__(self):
        super().__init__("table is occupied")

class Tableid(TableExceptions):
    def __init__(self):
        super().__init__("table id does not exist")

class Tableavail(TableExceptions):
    def __init__(self):
        super().__init__("table already availble")
