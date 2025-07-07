class Piece:
    def __init__(self, side: str, type: str):
        self.side = side
        self.type = type

    #Getter
    def get_side(self):
        return self.side

    def get_type(self):
        return self.type