import uuid

class Being:
    """
    Being is the AIUS top-level base class. Any class inherits from Beings
    """
    id = "Aius-Being"
    name = ""
    sensors = []
    memory = []
    processing = []
    tools = []

    def __init__(self):
        self.id = f"Aius-{self.__class__.__name__}-{uuid.uuid4()}"

    def __hash__(self):
        return super().__hash__()

    def __repr__(self):
        return self.id

    def __str__(self):
        return self.id

    def get_id(self):
        return self.id